import fs from "node:fs";
import path from "node:path";

const root = path.dirname(new URL(import.meta.url).pathname);
const corpusPath = path.join(root, "PROMPT_REGRESSION_CORPUS_2026-09-25.json");
const corpus = JSON.parse(fs.readFileSync(corpusPath, "utf8"));

const REQUIRED_CONTRACT = [
  "OBJECTIVE",
  "SCOPE",
  "DO-NOT-MIX",
  "AVAILABLE EVIDENCE",
  "EXECUTION",
  "FAILURE SEMANTICS",
  "VERIFICATION",
  "PERSISTENCE",
  "STOP / CONTINUE"
];

export function inspectPromptContract(prompt) {
  const normalized = String(prompt || "").toUpperCase();
  const missing = REQUIRED_CONTRACT.filter(section => !normalized.includes(section));
  return Object.freeze({ ok: missing.length === 0, missing });
}

export function evaluateCase(caseData, prompt) {
  const contract = inspectPromptContract(prompt);
  const text = String(prompt || "").toLowerCase();
  const propertyChecks = {
    evidence_preservation: /evidence|verified|verification|persist/.test(text),
    project_isolation: /project|do-not-mix|scope/.test(text),
    failure_handling: /failure|blocker|external|false-success/.test(text),
    duplicate_avoidance: /duplicate|dedup|existing/.test(text),
    tool_routing: /tool|github|railway|supabase|vercel|files/.test(text),
    completeness: /next frontier|continue|execution/.test(text)
  };
  return Object.freeze({
    id: caseData.id,
    contract,
    propertyChecks,
    pass: contract.ok && Object.values(propertyChecks).every(Boolean)
  });
}

export function evaluateCorpus(prompt) {
  return corpus.cases.map(item => evaluateCase(item, prompt));
}

if (import.meta.url === `file://${process.argv[1]}`) {
  const prompt = fs.readFileSync(process.stdin.fd, "utf8");
  const results = evaluateCorpus(prompt);
  process.stdout.write(JSON.stringify({
    schema_version: 1,
    cases: results,
    passed: results.filter(r => r.pass).length,
    total: results.length,
    status: results.every(r => r.pass) ? "CONTRACT_PASS" : "CONTRACT_FAIL",
    note: "This is a deterministic contract check, not a model-quality benchmark."
  }, null, 2));
}
