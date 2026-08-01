---
name: using-ai-surface-skills
description: >
  Route agent-tool / MCP work to the right AI Surface skill. Use when the user mentions
  tools, function calling, MCP tools, tool schema, permissions, human approval, agent
  retries, skill vs MCP, tool eval, or ship-check for tools. Also Chinese:
  "tool 契约", "MCP 工具面", "人审", "工具权限", "该用哪个 skill", "skill 还是 MCP".
  Do NOT use for REST OpenAPI evolution (use api-platform-skills) or MCP server scaffolding tutorials.
---

# Using AI Surface Skills

> Router only. One primary skill. Never load all nine.


## Overview

Pick the smallest AI Surface skill for the task. Do not load the whole pack.

## Routing

| Intent | Primary | Optional |
|--------|---------|----------|
| Design a new tool / function schema | `tool-contract-design` | `tool-permission-matrix` |
| Changed tool JSON / MCP tools list | `tool-schema-breaking-review` | - |
| Double charge / retry side effects | `tool-idempotency-and-retries` | - |
| Who can call which tool / blast radius | `tool-permission-matrix` | `human-approval-gates` |
| Dangerous action needs human confirm | `human-approval-gates` | - |
| Audit existing MCP server tools | `mcp-tool-surface-review` | `tool-permission-matrix` |
| Skill or MCP or both? | `skill-vs-mcp-choice` | - |
| Prove tools work / regression | `agent-tool-eval` | - |
| Pre-merge tool surface gate | Ship-check below | - |
| HTTP API field rename for humans | Out of scope -> api-platform-skills | - |
| How do I scaffold FastMCP? | Out of scope -> official mcp-builder | - |

## Ship-check sequence

1. `tool-contract-design` (or confirm contract exists)
2. `tool-schema-breaking-review`
3. `tool-permission-matrix`
4. Side effects -> `tool-idempotency-and-retries`
5. High risk -> `human-approval-gates`
6. Optional: `agent-tool-eval` smoke tasks

## Steps

1. Restate goal in one sentence.
2. Pick primary skill or out-of-scope.
3. Tell user which skill is active.
4. Execute to exit criteria.
5. Summarize.

## Exit criteria

- [ ] Primary skill chosen (or ship-check / out-of-scope)
- [ ] User informed
- [ ] Specialized exit criteria met

## Anti-patterns

- Loading every skill
- Answering with MCP scaffold code when asked about contract evolution
- Skipping break review for "small param renames"

## Output template

```markdown
## Skill routing
- Goal: ...
- Primary: `...`
- Secondary: `...` | none
- Mode: single | ship-check | out-of-scope
```
