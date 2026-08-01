---
name: skill-vs-mcp-choice
description: >
  Decide whether to use an Agent Skill, an MCP server, both, or neither. Use when
  choosing architecture for agent capabilities, or Chinese "skill 还是 MCP",
  "用 skill 还是 tool", "要不要做 MCP". Decision skill - not an implementation tutorial.
---

# Skill vs MCP Choice


## Overview

Choose skill, MCP, both, or plain code for a capability.

## Quick rules

| Need | Prefer |
|------|--------|
| Procedure / checklist / domain workflow in markdown | **Skill** |
| Live data, external API, stateful side effects | **MCP (or native tools)** |
| Both procedure + live calls | **Skill + MCP** |
| One-off script never reused | Neither - just code |

## Steps

1. Restate capability.
2. Ask: does it need **runtime I/O** beyond the repo?
3. Ask: is the value **how to think/work** vs **what to call**?
4. Recommend: skill | mcp | both | code-only.
5. If both: skill owns workflow; MCP owns tools; skill tells when to call which tool.

## Exit criteria

- [ ] Capability stated
- [ ] I/O vs procedure analyzed
- [ ] Clear recommendation
- [ ] If both: ownership split written

## Anti-patterns

- MCP for pure markdown procedures
- Skill that pretends to call APIs without tools
- Building MCP because it is trendy

## Output template

```markdown
## Choice
- Capability: ...
- Recommendation: skill | mcp | both | code-only
- Why: ...
- Split (if both): ...
```
