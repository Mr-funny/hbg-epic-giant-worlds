#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SKILLS = (
    "hbg-keyword-giant-world",
    "hbg-oriental-giant-world",
    "hbg-oriental-giant-roam",
)


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


manifest_path = ROOT / ".codex-plugin" / "plugin.json"
manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
if manifest.get("name") != "hbg-epic-giant-worlds":
    fail("unexpected plugin name")
if not re.fullmatch(r"\d+\.\d+\.\d+", str(manifest.get("version", ""))):
    fail("plugin version must be strict semver")

for skill_name in SKILLS:
    skill_dir = ROOT / "skills" / skill_name
    skill_file = skill_dir / "SKILL.md"
    agent_file = skill_dir / "agents" / "openai.yaml"
    if not skill_file.exists() or not agent_file.exists():
        fail(f"missing required files for {skill_name}")
    text = skill_file.read_text(encoding="utf-8")
    if "[TODO:" in text:
        fail(f"TODO remains in {skill_file}")
    if not text.startswith("---\nname: "):
        fail(f"invalid frontmatter in {skill_file}")
    if f"name: {skill_name}\n" not in text.split("---", 2)[1]:
        fail(f"frontmatter name mismatch in {skill_file}")

bank = ROOT / "skills" / "hbg-oriental-giant-roam" / "assets" / "prompt-bank.jsonl"
records = []
for line_number, raw in enumerate(bank.read_text(encoding="utf-8").splitlines(), 1):
    if not raw.strip():
        continue
    item = json.loads(raw)
    if not item.get("id"):
        fail(f"bank line {line_number} has no id")
    records.append(item)
if len(records) < 20:
    fail("packaged bank is unexpectedly small")

roam = ROOT / "skills" / "hbg-oriental-giant-roam" / "scripts" / "roam_prompts.py"
subprocess.run([sys.executable, str(roam), "--count", "4", "--seed", "2026", "--format", "json"], check=True, stdout=subprocess.DEVNULL)
print(f"OK: plugin, {len(SKILLS)} skills, and {len(records)} roam cards validated")
