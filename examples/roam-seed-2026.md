# Example: fixed-seed roam

Run:

```bash
python3 skills/hbg-oriental-giant-roam/scripts/roam_prompts.py \
  --bank skills/hbg-oriental-giant-roam/assets/prompt-bank.jsonl \
  --count 4 \
  --seed 2026 \
  --format markdown
```

This concise example intentionally uses the optional 24-card HBG archetype bank. Omit `--bank` to roam the default public archive of 475 source prompts. The selector prefers different camera, foreground, and scale-mechanism families. The Agent then treats each selected record as a semantic question, applies the fixed Eastern Colossal Style Lock, and rewrites the actual video prompt only after each mother image exists.
