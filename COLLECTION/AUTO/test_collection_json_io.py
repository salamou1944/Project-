import json
import subprocess
import tempfile
import unittest
from pathlib import Path

from collection_json_io import SHARD_SCHEMA, load_collection_json, write_collection_json


def atomic_writer(path, payload, compact_array_keys=None):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


class CollectionJsonIOTests(unittest.TestCase):
    def payload(self, count=250):
        return {
            "generated_at": "2026-10-22T00:00:00Z",
            "counts": {"items": count},
            "items": [
                {"capability_key": f"capability-{i:05d}", "description": "x" * 120, "evidence": [{"source": f"github:owner/repo-{i}"}]}
                for i in range(count)
            ],
        }

    def test_small_payload_stays_monolithic(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "PROMOTION-QUEUE.json"
            payload = self.payload(3)
            result = write_collection_json(path, payload, array_key="items", monolithic_writer=atomic_writer, threshold_bytes=1_000_000)
            self.assertEqual(result["format"], "monolithic")
            self.assertEqual(load_collection_json(path), payload)

    def test_sharded_round_trip_and_size_limit(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "READY.json"
            payload = self.payload(600)
            result = write_collection_json(path, payload, array_key="items", monolithic_writer=atomic_writer, threshold_bytes=1, max_shard_bytes=2048, initial_buckets=2)
            self.assertEqual(result["format"], "sharded")
            manifest = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(manifest["schema_version"], SHARD_SCHEMA)
            self.assertEqual(load_collection_json(path), payload)
            self.assertTrue(manifest["shards"])
            self.assertTrue(all(entry["bytes"] <= 2048 for entry in manifest["shards"]))

    def test_hash_mismatch_fails_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "READY.json"
            payload = self.payload(100)
            write_collection_json(path, payload, array_key="items", monolithic_writer=atomic_writer, threshold_bytes=1, max_shard_bytes=4096, initial_buckets=2)
            manifest = json.loads(path.read_text(encoding="utf-8"))
            shard = path.parent / manifest["shards"][0]["path"]
            shard.write_bytes(shard.read_bytes() + b" ")
            with self.assertRaisesRegex(ValueError, "SHA-256 mismatch"):
                load_collection_json(path)

    def test_git_baseline_reconstructs_shards_from_same_tree(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "READY.json"
            payload = self.payload(120)
            write_collection_json(path, payload, array_key="items", monolithic_writer=atomic_writer, threshold_bytes=1, max_shard_bytes=4096, initial_buckets=2)
            subprocess.run(["git", "init", "-q"], cwd=root, check=True)
            subprocess.run(["git", "config", "user.email", "collection-test@example.invalid"], cwd=root, check=True)
            subprocess.run(["git", "config", "user.name", "Collection JSON Test"], cwd=root, check=True)
            subprocess.run(["git", "add", "."], cwd=root, check=True)
            subprocess.run(["git", "commit", "-qm", "test shard manifest"], cwd=root, check=True)
            self.assertEqual(load_collection_json("READY.json", git_ref="HEAD", repo_root=root), payload)

    def test_rewrite_removes_old_shard_directories(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "READY.json"
            first = self.payload(200)
            second = self.payload(201)
            write_collection_json(path, first, array_key="items", monolithic_writer=atomic_writer, threshold_bytes=1, max_shard_bytes=4096, initial_buckets=2)
            first_dirs = {p.name for p in path.parent.glob("READY.json.parts-*") if p.is_dir()}
            write_collection_json(path, second, array_key="items", monolithic_writer=atomic_writer, threshold_bytes=1, max_shard_bytes=4096, initial_buckets=2)
            second_dirs = {p.name for p in path.parent.glob("READY.json.parts-*") if p.is_dir()}
            self.assertEqual(len(second_dirs), 1)
            self.assertNotEqual(first_dirs, second_dirs)
            self.assertEqual(load_collection_json(path), second)


if __name__ == "__main__":
    unittest.main()
