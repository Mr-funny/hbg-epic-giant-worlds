#!/usr/bin/env python3
"""Select reproducible prompt-bank questions for HBG Oriental Giant Roam."""

from __future__ import annotations

import argparse
import json
import random
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


DEFAULT_BANK = Path(__file__).resolve().parent.parent / "assets" / "prompt-bank.jsonl"


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, raw in enumerate(handle, 1):
            line = raw.strip()
            if not line:
                continue
            try:
                item = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"{path}:{line_number}: invalid JSON: {exc}") from exc
            if not isinstance(item, dict):
                raise ValueError(f"{path}:{line_number}: each line must be an object")
            item.setdefault("id", f"line-{line_number:04d}")
            records.append(item)
    if not records:
        raise ValueError(f"prompt bank is empty: {path}")
    return records


def search_blob(item: dict[str, Any]) -> str:
    values: list[str] = []
    for key, value in item.items():
        if isinstance(value, str):
            values.append(value)
        elif isinstance(value, list):
            values.extend(str(part) for part in value)
    return " ".join(values).lower()


def filter_records(records: list[dict[str, Any]], theme: str | None, source: str | None) -> list[dict[str, Any]]:
    result = records
    if theme:
        terms = [term.strip().lower() for term in theme.split(",") if term.strip()]
        result = [item for item in result if all(term in search_blob(item) for term in terms)]
    if source:
        wanted = source.lower()
        result = [
            item
            for item in result
            if wanted in str(item.get("source", "")).lower()
            or wanted in str(item.get("author", "")).lower()
            or wanted in str(item.get("post_url", "")).lower()
        ]
    return result


def load_history(path: Path | None) -> list[str]:
    if not path or not path.exists():
        return []
    ids: list[str] = []
    with path.open("r", encoding="utf-8") as handle:
        for raw in handle:
            try:
                item = json.loads(raw)
            except json.JSONDecodeError:
                continue
            if isinstance(item, dict) and item.get("id"):
                ids.append(str(item["id"]))
    return ids


def camera_family(item: dict[str, Any]) -> str:
    return str(item.get("camera_family") or item.get("camera") or "unknown")


def foreground_family(item: dict[str, Any]) -> str:
    return str(item.get("foreground_family") or "unknown")


def scale_mechanism(item: dict[str, Any]) -> str:
    value = item.get("scale_mechanism") or item.get("matched_giant_keywords") or "unknown"
    return json.dumps(value, ensure_ascii=False, sort_keys=True) if isinstance(value, (list, dict)) else str(value)


def select_diverse(records: list[dict[str, Any]], count: int, seed: int, recent_ids: set[str]) -> list[dict[str, Any]]:
    rng = random.Random(seed)
    pool = list(records)
    rng.shuffle(pool)
    fresh = [item for item in pool if str(item.get("id")) not in recent_ids]
    if len(fresh) >= count:
        pool = fresh

    selected: list[dict[str, Any]] = []
    used_camera: set[str] = set()
    used_foreground: set[str] = set()
    used_scale: set[str] = set()

    while pool and len(selected) < count:
        best_index = 0
        best_score = -1
        for index, item in enumerate(pool):
            score = 0
            score += 3 if camera_family(item) not in used_camera else 0
            score += 3 if foreground_family(item) not in used_foreground else 0
            score += 4 if scale_mechanism(item) not in used_scale else 0
            score += rng.random()
            if score > best_score:
                best_score = score
                best_index = index
        item = pool.pop(best_index)
        selected.append(item)
        used_camera.add(camera_family(item))
        used_foreground.add(foreground_family(item))
        used_scale.add(scale_mechanism(item))

    if len(selected) < count:
        raise ValueError(f"requested {count} records but only {len(selected)} matched")
    return selected


def provenance(item: dict[str, Any]) -> dict[str, Any]:
    return {
        key: item[key]
        for key in ("id", "source", "post_url", "author", "content_hash")
        if item.get(key) is not None
    }


def selection_package(item: dict[str, Any]) -> dict[str, Any]:
    raw_prompt = item.get("prompt")
    semantic_seed = item.get("semantic_seed") or item.get("seed_semantics")
    if not semantic_seed and raw_prompt:
        semantic_seed = "Extract the core spectacle, action, spatial mechanism, and emotional contradiction from the archived source prompt."
    return {
        "id": item.get("id"),
        "title": item.get("title", item.get("id")),
        "provenance": provenance(item),
        "semantic_seed": semantic_seed,
        "scale_mechanism": item.get("scale_mechanism", item.get("matched_giant_keywords", [])),
        "camera_family": item.get("camera_family", "choose a composition different from neighboring selections"),
        "foreground_family": item.get("foreground_family", "choose a non-repeating foreground family"),
        "cosmic_anchor": item.get("cosmic_anchor", "optional; at most one"),
        "motion_seed": item.get("motion_seed", "rewrite after inspecting the actual mother image"),
        "adaptation_instruction": "Preserve the semantic kernel and cultural identity; discard source style/composition wording; rebuild with HBG Eastern Colossal Style Lock v1.0.",
        "source_prompt_local_only": raw_prompt if raw_prompt else None,
    }


def render_markdown(packages: list[dict[str, Any]], seed: int, bank: Path) -> str:
    lines = [
        "# HBG Oriental Giant Roam selection",
        "",
        f"- Seed: `{seed}`",
        f"- Bank: `{bank}`",
        f"- Count: `{len(packages)}`",
        "",
        "> Treat each result as a question. Preserve semantics and provenance, then rewrite image and motion language with the fixed HBG Eastern Colossal Style Lock.",
        "",
    ]
    for index, item in enumerate(packages, 1):
        lines.extend(
            [
                f"## {index:02d}. {item['title']}",
                "",
                f"- ID: `{item['id']}`",
                f"- Semantic seed: {item.get('semantic_seed')}",
                f"- Scale mechanism: {item.get('scale_mechanism')}",
                f"- Camera family: {item.get('camera_family')}",
                f"- Foreground family: {item.get('foreground_family')}",
                f"- Cosmic anchor: {item.get('cosmic_anchor')}",
                f"- Motion seed: {item.get('motion_seed')}",
                f"- Provenance: `{json.dumps(item.get('provenance', {}), ensure_ascii=False)}`",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def record_history(path: Path, packages: list[dict[str, Any]], seed: int) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc).isoformat()
    with path.open("a", encoding="utf-8") as handle:
        for item in packages:
            handle.write(json.dumps({"id": item["id"], "seed": seed, "selected_at": now}, ensure_ascii=False) + "\n")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bank", type=Path, default=DEFAULT_BANK, help="JSONL question bank")
    parser.add_argument("--count", type=int, default=1, help="number of questions")
    parser.add_argument("--seed", type=int, default=None, help="deterministic random seed")
    parser.add_argument("--theme", help="comma-separated terms that must all match")
    parser.add_argument("--source", help="filter imported provenance by source/author/url")
    parser.add_argument("--history", type=Path, help="JSONL history used to avoid recent IDs")
    parser.add_argument("--record-history", type=Path, help="append selected IDs to this JSONL history")
    parser.add_argument("--format", choices=("json", "markdown"), default="json")
    parser.add_argument("--out", type=Path, help="write output to a file instead of stdout")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.count < 1:
        print("--count must be at least 1", file=sys.stderr)
        return 2
    seed = args.seed if args.seed is not None else random.SystemRandom().randrange(1, 2**31)
    try:
        records = load_jsonl(args.bank)
        records = filter_records(records, args.theme, args.source)
        if not records:
            raise ValueError("no records matched the requested filters")
        recent = set(load_history(args.history)[-20:])
        selected = select_diverse(records, args.count, seed, recent)
        packages = [selection_package(item) for item in selected]
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    payload = (
        render_markdown(packages, seed, args.bank)
        if args.format == "markdown"
        else json.dumps({"seed": seed, "bank": str(args.bank), "items": packages}, ensure_ascii=False, indent=2) + "\n"
    )
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(payload, encoding="utf-8")
    else:
        sys.stdout.write(payload)
    if args.record_history:
        record_history(args.record_history, packages, seed)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

