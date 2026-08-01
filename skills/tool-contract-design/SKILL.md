---
name: tool-contract-design
description: >
  Design high-quality agent tool / function-calling / MCP tool contracts. Use when
  defining tools, writing tool descriptions, JSON schemas for parameters, error
  shapes, or when the user says "design this tool", "tool schema", "function calling
  contract", or Chinese "设计 tool", "工具描述", "function schema", "MCP 工具设计".
  Focus on contract quality for agents - not scaffolding an MCP server project.
---

# Tool Contract Design

> Agents choose tools by name + description. Garbage contracts = wrong calls.

## Overview

Produce a complete **tool contract**: name, description (when to call / when not),
parameters schema, side-effect class, errors, idempotency notes. Framework-agnostic
(OpenAI tools, Anthropic tools, MCP `tools/list` shape).

## Steps

1. **State the job** - one sentence capability; name verbs carefully (`get_`, `list_`, `create_`, `delete_`).
2. **Describe for the model** - when to use, when NOT to use, prerequisites.
3. **Parameters** - required vs optional; enums; no grab-bag `metadata` objects without schema.
4. **Side-effect class** - read | write | money | external_network | destructive.
5. **Errors** - stable error codes the agent can branch on; no stack traces as contract.
6. **Idempotency** - natural key or client token if write.
7. **Examples** - one happy call + one invalid call.
8. **Emit** tool definition (JSON) + design notes.

## Exit criteria

- [ ] Name + description with when/when-not
- [ ] Parameters fully typed; required list explicit
- [ ] Side-effect class stated
- [ ] Error model noted
- [ ] Idempotency note for writes
- [ ] Happy + invalid examples

## Anti-patterns

- Description = "Does the thing"
- `input: object` with free-form anything
- Silent side effects not mentioned in description
- Overlapping tools that confuse routing
- Teaching FastMCP project layout instead of the contract

## Output template

```markdown
## Tool contract

### Definition (JSON)
```json
{ "name": "...", "description": "...", "parameters": { } }
```

### Side-effect class
read | write | money | external_network | destructive

### Idempotency
...

### Errors
| code | meaning | agent action |
|------|---------|--------------|

### Examples
- Happy: ...
- Invalid: ...

### Open questions
- ...
```
