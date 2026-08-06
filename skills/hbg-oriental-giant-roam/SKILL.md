---
name: hbg-oriental-giant-roam
description: Roam a built-in or user-imported prompt bank by random seed, theme, source, or visual mechanism, preserve each question's core spectacle, and adapt it into the same luminous Eastern colossal still-and-Veo style. Use for 漫游模式、随机抽题、提示词学习、题库探索、连续灵感、固定种子或批量东方巨物改写。
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

Use `--theme`, `--bank`, `--history`, and `--record-history` as needed. The packaged bank contains original HBG archetype cards, not copied third-party prompt prose. A user may import a local JSONL archive; never print, publish, commit, or upload it without explicit permission.

## Adaptation sequence

For each selected record:

1. Save or cite the source metadata separately.
2. Extract only the core spectacle, action, spatial mechanism, and emotional contradiction.
3. Discard the source's style adjectives, composition skeleton, model parameters, quality tags, and accidental clutter.
4. Rebuild the idea with the HBG Eastern Colossal Style Lock.
5. Choose a new foreground family, camera relationship, leading line, and light state.
6. Write a fresh 16:9 mother-image prompt.
7. After an actual still exists, write a fresh image-relative Veo/Gemini prompt.

Never present an imported prompt as original HBG writing. Keep `source_url`, `author`, `content_hash`, and provenance when available.

## Style invariance

Across an entire roaming session, keep these fixed unless the user changes them:

- luminous, airy, auspicious Eastern cinematic realism;
- blue-white atmosphere with restrained warm gold and culturally appropriate materials;
- realistic air perspective and premium environment detail;
- tiny people, one dominant giant form, one optional cosmic anchor;
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
Eastern colossal adaptation thesis
Composition and camera change
Mother-image prompt
Image-relative motion prompt or motion plan
Risk and cultural checks
```

If no actual image has been generated, label the video text as a motion plan. Do not falsely claim it is image-relative.

## Generation and delivery

When the user asks to generate, produce each mother image independently, inspect it, visibly render it in chat, save the prompt, and then adapt motion from that image. For four videos, verify each clip independently and stitch only after architecture, people, scale, motion, codec, and aspect ratio pass QA.

