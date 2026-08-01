# Toy tools fixtures

OpenAI-style `tools` arrays for skill demos.

| File | Intent |
|------|--------|
| `tools.v1.json` | Shipped baseline |
| `tools.v1.1-safe.json` | Additive only -> approve |
| `tools.v2-bad.json` | Silent breaks + unsafe tools -> request-changes |

## Prompt

```text
Compare tools.v1.json and tools.v2-bad.json with tool-schema-breaking-review.
Also run tool-permission-matrix on v2-bad.
```
