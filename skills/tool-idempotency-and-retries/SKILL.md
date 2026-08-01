---
name: tool-idempotency-and-retries
description: >
  Design idempotent agent tools under retries and timeouts. Use when tools create
  payments/orders/messages, agents re-call tools after timeout, or user says
  "tool idempotency", "retry safe tool", or Chinese "工具幂等", "agent 重试", "重复调用".
---

# Tool Idempotency and Retries

> Agents retry. Networks flake. Side effects must not double.


## Overview

Make write tools safe under agent retries and timeouts.

## Steps

1. Classify each tool: pure read | idempotent write | unsafe create | external side effect.
2. Choose mechanism: natural key param, `idempotency_key` param, server dedupe store.
3. Define conflict: same key different args -> error.
4. Document retry guidance for the agent (when to retry, when to stop).
5. Tests: sequential double call, concurrent double call, body mismatch.

## Exit criteria

- [ ] Tools classified
- [ ] Mechanism per write tool
- [ ] Conflict + TTL semantics
- [ ] Agent retry policy
- [ ] Test cases listed

## Anti-patterns

- "Just call create again"
- Accepting keys without storing them
- Retrying non-idempotent tools blindly

## Output template

```markdown
## Tool idempotency design
| tool | class | mechanism | conflict | agent retry |
|------|-------|-----------|----------|-------------|
```
