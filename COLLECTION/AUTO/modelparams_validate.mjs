#!/usr/bin/env node
/**
 * Validate model parameters using the exact modelparams package vendored by Collection.
 *
 * Prerequisites: run npm ci --ignore-scripts in the installed asset root and
 * build it with npm run build --workspace packages/modelparams.
 *
 * Usage:
 *   node COLLECTION/AUTO/modelparams_validate.mjs openai/gpt-4.1 '{"temperature":0.5}'
 *   node COLLECTION/AUTO/modelparams_validate.mjs --expect-invalid openai/gpt-4.1 '{"frequency_penalty":0.5}'
 */
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const collectionRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const installedRoot = path.join(collectionRoot, "INSTALLED", "mnfst__modelparams.dev");
const runtimeEntry = path.join(installedRoot, "packages", "modelparams", "dist", "index.js");

function fail(message, code = 2) {
  console.error(JSON.stringify({ ok: false, error: message }));
  process.exitCode = code;
}

async function main() {
  const args = process.argv.slice(2);
  if (args.includes("--help") || args.length === 0) {
    console.log("Usage: node COLLECTION/AUTO/modelparams_validate.mjs [--expect-invalid] <provider/model> <params-json>");
    return;
  }
  const expectInvalid = args[0] === "--expect-invalid";
  if (expectInvalid) args.shift();
  if (args.length !== 2) return fail("expected model ID and one JSON object argument");
  if (!fs.existsSync(runtimeEntry)) {
    return fail("installed package is not built; run npm ci --ignore-scripts and npm run build --workspace packages/modelparams in COLLECTION/INSTALLED/mnfst__modelparams.dev");
  }

  let params;
  try {
    params = JSON.parse(args[1]);
  } catch {
    return fail("params argument is not valid JSON");
  }

  const { parseParams, resolveModelId } = await import(pathToFileURL(runtimeEntry).href);
  const resolved = resolveModelId(args[0]);
  if (!resolved.ok) {
    return fail("model ID did not resolve: " + JSON.stringify(resolved));
  }

  const result = parseParams(resolved.id, params);
  if (expectInvalid) {
    if (result.success) return fail("expected invalid parameters, but validation succeeded", 1);
    console.log(JSON.stringify({ ok: true, status: "EXPECTED_REJECTION", modelId: resolved.id, issues: result.issues }));
    return;
  }
  if (!result.success) {
    console.log(JSON.stringify({ ok: false, status: "REJECTED", modelId: resolved.id, issues: result.issues }));
    process.exitCode = 2;
    return;
  }
  console.log(JSON.stringify({ ok: true, status: "ACCEPTED", modelId: resolved.id, params: result.value }));
}

main().catch((error) => fail(error instanceof Error ? error.message : String(error), 1));
