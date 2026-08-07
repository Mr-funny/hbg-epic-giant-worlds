---
name: hbg-oriental-giant-roam
description: Roam the bundled public 475-prompt Eastern colossal archive, the optional HBG archetype bank, or a user-provided bank; preserve provenance and transmute each selected idea into the same luminous, absurd, ontologically impossible Eastern giant-construct still-and-Veo style. Use for 漫游模式、随机抽题、提示词原文学习、万物皆可巨构、荒诞巨物、题库探索、连续灵感或批量东方巨物改写。
---

# HBG Oriental Giant Roam

Use prompt collections as a question bank, not as a style master. Preserve the selected idea's semantic surprise while rewriting every result into one stable Eastern Colossal image-and-video grammar.

## Read first

- Read `references/roam-protocol.md` completely.
- Read `references/oriental-style-lock.md` completely.
- Use `scripts/roam_prompts.py` to select questions reproducibly.
- For actual image or video generation, read the environment's image and mandatory video skills.

## Modes

- `random`: sample without a theme.
- `theme`: filter by words such as moon, waterfall, deity, city, gate, ocean, planet, pilgrimage.
- `source`: filter an imported JSONL bank by source or author metadata.
- `mechanism`: explore one scale device such as tiny humans, planetary horizon, cliff-city, giant relief, impossible road, or cloud ocean.
- `study`: show source archive, semantic extraction, adaptation decisions, and final prompts side by side.

Accept count and seed when supplied. If absent, default to one question and a random seed. For a four-shot montage, select four records with different camera and foreground families.

## Selection command

```bash
python3 scripts/roam_prompts.py --count 4 --seed 2026 --format markdown
```

Use `--theme`, `--bank`, `--history`, and `--record-history` as needed. The default packaged bank is `assets/public-eastern-giant-prompts.jsonl`: 475 public source prompts with author, source URL, and content hash. Use `--bank assets/prompt-bank.jsonl` to switch to the 24 HBG-authored abstract mechanism cards. A user may also import a private JSONL archive; never publish, commit, or upload a private archive without explicit permission.

## Adaptation sequence

For each selected record:

1. Show the selected source prompt and preserve its source metadata separately.
2. Extract only the core spectacle, action, spatial mechanism, and emotional contradiction.
3. Discard the source's style adjectives, composition skeleton, model parameters, quality tags, and accidental clutter.
4. Reject any version that remains a plausible temple, landmark, village, statue, mountain, or tourist landscape.
5. Transmute the semantic kernel into an inhabited world-body by fusing at least two categories and adding one impossible law with visible environmental consequences.
6. Require three independent scale proofs and a dominant giant form before proceeding.
7. Rebuild the idea with the HBG Eastern Colossal Style Lock.
8. Choose a new foreground family, camera relationship, leading line, and light state.
9. Write a fresh 16:9 mother-image prompt.
10. After an actual still exists, write a fresh image-relative Veo/Gemini prompt.

Never present a third-party prompt as original HBG writing. Keep `post_url`, `author`, `content_hash`, and provenance when available. The repository's MIT license does not grant new rights to third-party prompt text.

## Style invariance

Across an entire roaming session, keep these fixed unless the user changes them:

- luminous, airy, auspicious Eastern cinematic realism;
- blue-white atmosphere with restrained warm gold and culturally appropriate materials;
- realistic air perspective and premium environment detail;
- tiny people visibly inhabiting one dominant impossible giant construct, with three scale proofs and one optional cosmic anchor;
- slow stabilized image-relative motion and rigid architecture;
- no default gloomy horror, neon sci-fi, character close-up, or copied reference layout.

Vary subject matter, camera, foreground, landscape, scale mechanism, and motion path. “Style fixed” does not mean “composition fixed.”

## Study-mode output

Return this structure for every question:

```text
Question ID and provenance
Source semantic kernel
What is preserved
What is discarded
Reality baseline rejected
Giant transmutation and category collision
Impossible law and visible consequences
Human inhabitation and three scale proofs
Eastern colossal adaptation thesis
Composition and camera change
Mother-image prompt
Image-relative motion prompt or motion plan
Risk and cultural checks
```

If no actual image has been generated, label the video text as a motion plan. Do not falsely claim it is image-relative.

## Generation and delivery

When the user asks to generate, produce each mother image independently, inspect it, visibly render it in chat, save the prompt, and then adapt motion from that image. For four videos, verify each clip independently and stitch only after architecture, people, scale, motion, codec, and aspect ratio pass QA.
