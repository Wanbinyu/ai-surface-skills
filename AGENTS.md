# AGENTS.md — AI Surface Skills

1. Optimize for **safe, evolvable tool contracts** agents call — not MCP server scaffolding tutorials.
2. Prefer least privilege: default tools to read-only; escalate write/network/money with `human-approval-gates`.
3. Never rename or retype a shipped tool parameter without `tool-schema-breaking-review`.
4. Side-effecting tools need an idempotency story under agent retries (`tool-idempotency-and-retries`).
5. Do not re-teach REST OpenAPI evolution — link [api-platform-skills](https://github.com/Wanbinyu/api-platform-skills).
6. Load one primary skill via `using-ai-surface-skills`; never dump all skills into context.
