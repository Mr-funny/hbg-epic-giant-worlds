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

keyword_skill = ROOT / "skills" / "hbg-keyword-giant-world"
transmutation = keyword_skill / "references" / "colossal-transmutation.md"
if not transmutation.exists():
    fail("missing colossal transmutation reference")
keyword_text = (keyword_skill / "SKILL.md").read_text(encoding="utf-8")
transmutation_text = transmutation.read_text(encoding="utf-8")
for required_phrase in ("Everything can become", "Reality-rejection gate", "Absurdity score"):
    if required_phrase not in keyword_text and required_phrase not in transmutation_text:
        fail(f"keyword giant-world system is missing required mechanism: {required_phrase}")

assets = ROOT / "skills" / "hbg-oriental-giant-roam" / "assets"


def load_bank(path: Path) -> list[dict]:
    records = []
    for line_number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip():
            continue
        item = json.loads(raw)
        if not item.get("id"):
            fail(f"{path.name} line {line_number} has no id")
        records.append(item)
    return records


archetypes = load_bank(assets / "prompt-bank.jsonl")
if len(archetypes) < 24:
    fail("HBG archetype bank is unexpectedly small")

public_prompts = load_bank(assets / "public-eastern-giant-prompts.jsonl")
if len(public_prompts) < 400:
    fail("public source-prompt bank is unexpectedly small")
required_source_fields = ("prompt", "post_url", "author", "content_hash")
for item in public_prompts:
    missing = [field for field in required_source_fields if not item.get(field)]
    if missing:
        fail(f"public prompt {item['id']} is missing: {', '.join(missing)}")
if len({item["id"] for item in public_prompts}) != len(public_prompts):
    fail("public prompt IDs must be unique")
if len({item["content_hash"] for item in public_prompts}) != len(public_prompts):
    fail("public prompt hashes must be unique")

roam = ROOT / "skills" / "hbg-oriental-giant-roam" / "scripts" / "roam_prompts.py"
result = subprocess.run(
    [sys.executable, str(roam), "--count", "4", "--seed", "2026", "--format", "json"],
    check=True,
    capture_output=True,
    text=True,
)
selection = json.loads(result.stdout)
if not str(selection.get("bank", "")).endswith("public-eastern-giant-prompts.jsonl"):
    fail("default roam bank is not the public source-prompt bank")
if any(not item.get("source_prompt") for item in selection.get("items", [])):
    fail("default roam output must include selected source prompts")
print(
    f"OK: plugin, {len(SKILLS)} skills, {len(public_prompts)} public prompts, "
    f"and {len(archetypes)} HBG archetype cards validated"
)
