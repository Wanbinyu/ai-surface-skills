# Not another MCP builder

## Positioning

```text
  BUILD server                    USE one product MCP
  (scaffold FastMCP/SDK)          (install-foo-mcp)
         │                                  │
         ▼                                  ▼
  anthropics/mcp-builder          product skill packs
  microsoft mcp-builder
         │
         │   orthogonal
         ▼
  ┌─────────────────────────────────────┐
  │  THIS PACK — ai-surface-skills      │
  │  tool contracts · breaking review   │
  │  idempotency · permissions · HITL   │
  │  MCP surface audit · tool eval      │
  └─────────────────────────────────────┘
```

## Side-by-side

| Topic | mcp-builder etc. | This pack |
|-------|------------------|-----------|
| Create MCP server project | Yes | No |
| Design tool name/description/schema well | Partial | **Yes** |
| Tool schema breaking changes | Rare | **Yes** |
| Agent retry double-execution | Rare | **Yes** |
| Permission blast radius | Rare | **Yes** |
| Human approval gates | Ad hoc | **Yes** |
| Review existing MCP tools list | Rare | **Yes** |
| Skill vs MCP choice | Blog posts | **Yes** (one skill) |

## Name collision policy

Avoid: `mcp-builder`, `api-design`, `security-review`, bare `agent-eval`.  
Prefer: `tool-contract-design`, `tool-schema-breaking-review`, `agent-tool-eval`.
