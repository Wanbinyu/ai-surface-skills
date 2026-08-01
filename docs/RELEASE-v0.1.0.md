## AI Surface Skills v0.1.0

Agent skills for **tool / MCP / function-calling surfaces** — design, evolution, permissions, human gates, eval.

**Not** an MCP server Hello World (see [NOT-ANOTHER-MCP-BUILDER](https://github.com/Wanbinyu/ai-surface-skills/blob/main/docs/NOT-ANOTHER-MCP-BUILDER.md)).

### Demo

- GIF: `assets/demo-tool-break.gif`
- Fixtures: `examples/toy-tools/tools.v1.json` vs `tools.v2-bad.json`
- Golden: `examples/sample-reports/tool-breaking-v1-vs-v2-bad.md`

### Skills (9)

| Skill | Job |
|-------|-----|
| using-ai-surface-skills | Router + ship-check |
| tool-contract-design | Design tool contracts |
| tool-schema-breaking-review | Breaking review for tools |
| tool-idempotency-and-retries | Safe retries |
| tool-permission-matrix | Blast radius |
| human-approval-gates | HITL |
| mcp-tool-surface-review | Audit existing MCP tools |
| skill-vs-mcp-choice | Skill vs MCP |
| agent-tool-eval | Minimal tool-use eval |

### Install

```powershell
git clone https://github.com/Wanbinyu/ai-surface-skills.git
cd ai-surface-skills
.\scripts\install.ps1 -Claude
```

### Sister pack

- [api-platform-skills](https://github.com/Wanbinyu/api-platform-skills) — HTTP / OpenAPI evolution for humans & SDKs

MIT · [Wanbinyu](https://github.com/Wanbinyu)
