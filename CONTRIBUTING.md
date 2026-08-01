# Contributing

## Accept

- Deeper exit criteria / better templates for **tool contract** topics
- Golden reports under `examples/sample-reports/`
- Install / harness fixes

## Reject

- MCP server Hello World tutorials (see anthropics mcp-builder)
- Product-specific "install Foo MCP" skills
- REST api-design clones
- AI-slop bulk skills without exit criteria

## Skill bar

Every `skills/<name>/SKILL.md` needs: frontmatter name+description, Overview, Steps, Exit criteria (checkboxes), Anti-patterns, Output template.

```bash
python scripts/validate_skills.py
gh search code "name: your-skill-name" --filename SKILL.md --limit 10
```
