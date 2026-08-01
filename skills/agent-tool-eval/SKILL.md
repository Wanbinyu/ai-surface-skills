---
name: agent-tool-eval
description: >
  Define a minimal evaluation set for agent tool use. Use when measuring if tools or
  prompts improved, regression after schema changes, or Chinese "tool 评测",
  "agent 回归", "工具调用评估". Lightweight task packs - not a full ML platform.
---

# Agent Tool Eval

> If you cannot state pass/fail, you are guessing.


## Overview

Define a small pass/fail task pack for tool-use quality.

## Steps

1. Pick 3-10 tasks (natural language goals).
2. For each: allowed tools, expected tool sequence (or set), forbidden tools, success criteria.
3. Define scoring: exact tool name | args constraints | outcome checks.
4. Baseline: run once without change; record.
5. After change: re-run; report pass rate + failures.

## Exit criteria

- [ ] Task list (>=3)
- [ ] Per-task success criteria
- [ ] Forbidden tools noted
- [ ] Scoring method
- [ ] Baseline or plan to capture baseline

## Anti-patterns

- Only vibes ("seems better")
- 100 flaky LLM-judge tasks with no structure
- Tasks that need prod credentials without sandbox

## Output template

```markdown
## Tool eval pack
| id | user goal | expected tools | success | forbidden |
|----|-----------|----------------|---------|-----------|
### Scoring
- ...
### Results
| id | pass/fail | notes |
```
