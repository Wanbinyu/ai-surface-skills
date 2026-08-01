---
name: human-approval-gates
description: >
  Design human-in-the-loop approval for high-risk agent tools. Use when tools delete
  data, spend money, send messages externally, change prod, or user says "human
  approval", "confirm before run", or Chinese "人审", "二次确认", "危险操作确认".
---

# Human Approval Gates

> If undo is hard or money moves, a human must say yes.

## Steps

1. List candidate tools (from permission matrix or inventory).
2. For each: risk reason, approval prompt text (what/why/blast radius), timeout behavior (deny by default).
3. Define who can approve (user vs role).
4. Logging: store decision for audit.
5. Never allow silent re-approval loops without new context.

## Exit criteria

- [ ] HITL tool list
- [ ] Prompt template per tool or class
- [ ] Default on timeout: deny
- [ ] Audit log fields
- [ ] Bypass policy (if any) documented and narrow

## Anti-patterns

- Auto-approve after N seconds
- Vague "are you sure?" without naming the action
- Burying destructive tools without gates

## Output template

```markdown
## Human approval design
| tool | risk | approval prompt summary | timeout | auditor fields |
|------|------|-------------------------|---------|----------------|
```
