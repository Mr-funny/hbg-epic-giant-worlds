# Roam protocol and provenance contract

## Purpose

Roaming is a learning and discovery mode. A selected prompt is a question to reinterpret, not a finished style to imitate.

## Three layers

1. Source archive: original text and provenance, stored separately and unchanged.
2. Semantic kernel: a short factual description of the wonder, action, spatial mechanism, and emotional contradiction.
3. HBG adaptation: wholly rewritten composition, still prompt, and image-relative motion language using the Style Lock.

Never overwrite layer 1 with layer 3. Never label a third-party source as HBG-authored.

## Packaged banks

The Skill ships with two banks:

1. `assets/public-eastern-giant-prompts.jsonl` is the default bank. It contains 475 public source prompts and retains `prompt`, `post_url`, `author`, and `content_hash` for study and traceability.
2. `assets/prompt-bank.jsonl` contains 24 HBG-authored abstract mechanism cards. Select it explicitly when the user wants compressed archetypes instead of source prose.

Keep source text unchanged in layer 1. Do not rename third-party writing as HBG-authored content. See the repository's `THIRD_PARTY_PROMPTS.md` for attribution and rights boundaries.

## User-provided banks

`scripts/roam_prompts.py --bank /absolute/path/archive.jsonl` accepts either archetype records or common archive records containing `id`, `prompt`, `post_url`, `author`, and `content_hash`.

Treat a user-provided private bank as private unless the user explicitly authorizes publication:

- do not commit or upload it automatically;
- display only records needed for the current request;
- preserve source URL, author, and hash when present;
- follow applicable source terms and law.

## Diversity gate for four questions

Choose four records that differ across:

- scale mechanism;
- camera family;
- foreground family;
- leading line;
- giant-form category;
- environmental or cosmic anchor;
- motion path.

If deterministic sampling produces near-duplicates, keep the seed but advance through the shuffled bank until diversity passes.

## Adaptation checklist

- Can the source's core surprise be stated in one sentence?
- Which details are cultural facts, and which are merely source styling?
- Has the adaptation rejected ordinary scenic tourism and merely enlarged landmarks?
- Does the selected idea become an inhabited world-body through category collision?
- Is there one impossible law with visible consequences and at least three scale proofs?
- Is the new composition structurally different?
- Does the result obey the fixed luminous Eastern Style Lock?
- Is regional identity preserved?
- Are tiny people and one giant form readable?
- Is the video text based on an actual image? If not, is it labeled provisional?
- Are provenance fields retained?
