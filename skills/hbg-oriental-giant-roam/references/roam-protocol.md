# Roam protocol and provenance contract

## Purpose

Roaming is a learning and discovery mode. A selected prompt is a question to reinterpret, not a finished style to imitate.

## Three layers

1. Source archive: original text and provenance, stored separately and unchanged.
2. Semantic kernel: a short factual description of the wonder, action, spatial mechanism, and emotional contradiction.
3. HBG adaptation: wholly rewritten composition, still prompt, and image-relative motion language using the Style Lock.

Never overwrite layer 1 with layer 3. Never label a third-party source as HBG-authored.

## Packaged bank

`assets/prompt-bank.jsonl` contains original HBG archetype cards derived from broad visual mechanisms. It contains no copied third-party prompt prose. Each record specifies semantic seed, scale mechanism, recommended variation, and motion seed.

## Local import

`scripts/roam_prompts.py --bank /absolute/path/archive.jsonl` accepts either archetype records or common archive records containing `id`, `prompt`, `post_url`, `author`, and `content_hash`.

Imported raw text is local-only by default:

- do not commit it;
- do not upload it;
- do not paste the entire bank into chat;
- display only records needed for the user's current study request;
- preserve source URL, author, and hash when present;
- follow the source site's terms and applicable copyright law.

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
- Is the new composition structurally different?
- Does the result obey the fixed luminous Eastern Style Lock?
- Is regional identity preserved?
- Are tiny people and one giant form readable?
- Is the video text based on an actual image? If not, is it labeled provisional?
- Are provenance fields retained?

