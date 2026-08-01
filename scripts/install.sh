#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="$ROOT/skills"
PROJECT=0; CLAUDE=0; ALL=0
for arg in "$@"; do
  case "$arg" in
    --project|-p) PROJECT=1 ;;
    --claude|-c) CLAUDE=1 ;;
    --all|-a) ALL=1 ;;
  esac
done
copy_skills() {
  local dest="$1"
  mkdir -p "$dest"
  for d in "$SRC"/*; do
    [ -d "$d" ] || continue
    name="$(basename "$d")"
    rm -rf "$dest/$name"
    cp -R "$d" "$dest/$name"
    echo "  + $name -> $dest/$name"
  done
}
if [ "$PROJECT" -eq 0 ] && [ "$CLAUDE" -eq 0 ] && [ "$ALL" -eq 0 ]; then CLAUDE=1; fi
if [ "$CLAUDE" -eq 1 ] || [ "$ALL" -eq 1 ]; then
  copy_skills "$HOME/.claude/skills"
fi
if [ "$ALL" -eq 1 ]; then
  copy_skills "$HOME/.agents/skills"
  copy_skills "$HOME/.cursor/skills"
fi
if [ "$PROJECT" -eq 1 ]; then
  for rel in .claude/skills .agents/skills .cursor/skills .github/skills; do
    copy_skills "$PWD/$rel"
  done
fi
echo "Done. Restart Claude Code."
