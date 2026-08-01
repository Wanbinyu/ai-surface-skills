---
name: tool-permission-matrix
description: >
  Build a permission and blast-radius matrix for agent tools. Use when deciding which
  tools an agent may call, least privilege, or Chinese "工具权限", "爆炸半径",
  "最小权限", "tool 白名单". Defensive product control - not penetration testing.
---

# Tool Permission Matrix

> Every tool is a privilege. Default deny for write/money/network.


## Overview

Map tools to privileges and least-privilege agent modes.

## Steps

1. Inventory tools.
2. Tag each: data sensitivity (public/PII/secret), effect (read/write/delete/money/network), reversibility.
3. Map roles or agent modes (read-only assistant, coder, admin) to allowed tools.
4. Flag tools that must never be auto-run (`human-approval-gates`).
5. Recommend default policy: allowlist vs denylist.

## Exit criteria

- [ ] Inventory complete
- [ ] Tags per tool
- [ ] Role x tool matrix
- [ ] HITL candidates listed
- [ ] Default policy stated

## Anti-patterns

- All tools enabled "for convenience"
- Ignoring network egress tools
- Treating UUID ids as authorization

## Output template

```markdown
## Permission matrix
| tool | effect | sensitivity | read-only agent | coder agent | admin | HITL? |
|------|--------|-------------|-----------------|-------------|-------|-------|
### Default policy
- ...
```
