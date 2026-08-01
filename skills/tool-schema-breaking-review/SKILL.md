---
name: tool-schema-breaking-review
description: >
  Review breaking changes to agent tool schemas or MCP tool lists. Use on PRs that
  rename tools/params, change types, add required fields, or change side effects; or
  when the user says "is this tool change breaking?", "/tool-break", or Chinese
  "tool 破坏性变更", "改了 schema 能合并吗", "工具改名". Requires migration notes or waiver.
---

# Tool Schema Breaking Review

> Merge verdict for agent-facing tools - not HTTP OpenAPI (use api-platform-skills for that).

## Catalog

**Usually breaking**

| Change | Why |
|--------|-----|
| Rename tool or param | Agents/prompts hardcode names |
| Remove tool/param | Callers fail |
| Type tighten / optional -> required | Old calls invalid |
| Enum value removed | |
| Side effect class escalates (read -> write) | Safety |
| Auth/scope newly required | |

**Usually non-breaking**

- New optional param
- New tool
- Description clarify without semantic flip
- New enum value if agents tolerate unknowns

## Steps

1. Load before/after (`examples/toy-tools/*.json` or repo tools).
2. List discrete deltas (one row each).
3. Classify each: non-breaking | breaking | semantic-breaking | unclear.
4. Migration or waiver per break.
5. Docs: agent prompts, skill docs, MCP clients to update.
6. Verdict.

## Exit criteria

- [ ] Before/after sources named
- [ ] All deltas classified
- [ ] Breaks have migration or waiver
- [ ] Merge verdict stated
- [ ] Template report filled

## Anti-patterns

- "Just a rename" without updating prompts
- Approving required-new fields on shipped tools without version
- Confusing HTTP API breaks with tool breaks

## Output template

```markdown
## Tool schema breaking review

### Scope
- Before: `...`
- After: `...`
- Maturity: shipped | experimental

### Deltas
| # | delta | class | migration |
|---|-------|-------|-----------|

### Verdict
- **request-changes** | **approve** | **approve-with-version** | **waiver-documented**
- Rationale: ...
```

## References

- Fixtures: `examples/toy-tools/`
- Golden: `examples/sample-reports/tool-breaking-v1-vs-v2-bad.md`
