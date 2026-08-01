#!/usr/bin/env python3
from __future__ import annotations
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
REQUIRED = ["## Overview", "## Steps", "## Exit criteria", "## Anti-patterns", "## Output template"]

def parse_fm(text: str):
    if not text.startswith("---"):
        raise ValueError("missing frontmatter")
    end = text.find("\n---", 3)
    if end < 0:
        raise ValueError("unterminated frontmatter")
    raw, body = text[3:end].strip(), text[end + 4 :]
    meta, key, chunks = {}, None, []
    for line in raw.splitlines():
        if re.match(r"^[a-zA-Z0-9_-]+:\s*", line) and not line.startswith(" "):
            if key is not None:
                meta[key] = "\n".join(chunks).strip()
            key, _, rest = line.partition(":")
            key, rest = key.strip(), rest.strip()
            chunks = [] if rest in (">", "|") else [rest]
        else:
            chunks.append(line.strip())
    if key:
        meta[key] = "\n".join(chunks).strip()
    return meta, body

def validate(path: Path) -> list[str]:
    errs = []
    raw = path.read_bytes()
    if b"\xef\xbf\xbd" in raw:
        errs.append("bad encoding U+FFFD")
    text = path.read_text(encoding="utf-8")
    try:
        meta, body = parse_fm(text)
    except ValueError as e:
        return [str(e)]
    if meta.get("name", "").strip() != path.parent.name:
        errs.append(f"name != folder ({meta.get('name')!r})")
    if not meta.get("description") or len(meta["description"]) < 40:
        errs.append("description missing or too short")
    for s in REQUIRED:
        if s not in body:
            errs.append(f"missing {s}")
    if "- [ ]" not in body:
        errs.append("need checkbox exit criteria")
    return errs

def main() -> int:
    failed = 0
    for d in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
        skill = d / "SKILL.md"
        if not skill.exists():
            print(f"FAIL {d.name}: no SKILL.md"); failed += 1; continue
        errs = validate(skill)
        if errs:
            print(f"FAIL {d.name}:"); [print(f"  - {e}") for e in errs]; failed += 1
        else:
            print(f"OK   {d.name}")
    print(f"\n{'FAIL' if failed else 'All OK'} ({failed} failed)" if failed else f"\nAll {len(list(SKILLS.iterdir()))} skills valid")
    return 1 if failed else 0

if __name__ == "__main__":
    raise SystemExit(main())
