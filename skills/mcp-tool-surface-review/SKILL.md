---
name: mcp-tool-surface-review
description: >
  Review an existing MCP server's tool surface for safety and clarity. Use when auditing
  tools/list output, third-party MCP installs, or Chinese "审查 MCP 工具", "MCP 安全面",
  "tools/list 审计". Does NOT teach how to scaffold a new MCP server (use official mcp-builder).
---

# MCP Tool Surface Review

> You already have an MCP. Are its tools safe for an agent to see?

## Steps

1. Obtain tool list (MCP `tools/list` dump or docs).
2. Per tool: description quality, param width, side effects, secrets in args, path traversal, SSRF-ish URL params.
3. Flag tool poisoning patterns: descriptions that instruct the model to ignore policy, exfiltrate, or hide actions.
4. Cross-check with `tool-permission-matrix` tags.
5. Verdict: allow / allow-with-HITL / block / fork-and-narrow.

## Exit criteria

- [ ] Tool inventory
- [ ] Findings table with severity
- [ ] Poisoning/over-broad params checked
- [ ] Verdict per tool or overall
- [ ] No exploit payload development

## Anti-patterns

- Rewriting the whole server in the review
- Generic "MCP is dangerous" without tool rows
- Shipping exploit chains

## Output template

```markdown
## MCP tool surface review
| tool | issue | severity | recommendation |
|------|-------|----------|----------------|
### Overall
- allow | harden | block
```
