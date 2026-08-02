# AI Surface Skills

**English** | [中文](README.zh-CN.md)

<p align="center">
  <strong>Stop agents from misusing tools and MCP.</strong><br/>
  <em>HTTP contracts evolve. Tool contracts should too.</em>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT" /></a>
  <a href="https://github.com/agentskills/agentskills"><img src="https://img.shields.io/badge/format-Agent%20Skills-111827" alt="Agent Skills" /></a>
  <img src="https://img.shields.io/badge/version-0.1.1-0ea5e9" alt="v0.1.1" />
  <img src="https://img.shields.io/badge/Claude-Codex-Cursor-7c3aed" alt="harnesses" />
</p>

---

## Start here (60 seconds)

### 1. Install (Claude Code)

```powershell
git clone https://github.com/Wanbinyu/ai-surface-skills.git
cd ai-surface-skills
.\scripts\install.ps1 -Claude
```

```bash
git clone https://github.com/Wanbinyu/ai-surface-skills.git
cd ai-surface-skills
chmod +x scripts/install.sh && ./scripts/install.sh --claude
```

Restart Claude Code → skills in `~/.claude/skills/`.

### 2. Try this prompt

```text
Compare examples/toy-tools/tools.v1.json with tools.v2-bad.json.
Follow tool-schema-breaking-review. Give a merge verdict.
Also flag permission risks on v2-bad.
```

**Expected:** `request-changes` — tool rename, required params tightened, cross-user list wording, `refund_order` without human gate.

<p align="center">
  <img src="assets/demo-tool-break.gif" alt="Demo: tool break review" width="800" />
</p>

---

## Why you need this

| Pain | Skill that helps |
|------|------------------|
| Agent renames a tool → all prompts break | **tool-schema-breaking-review** |
| Timeout retry creates two orders | **tool-idempotency-and-retries** |
| Refund / delete tools always-on | **tool-permission-matrix** + **human-approval-gates** |
| Third-party MCP with vague dangerous tools | **mcp-tool-surface-review** |
| “Should this be a skill or MCP?” | **skill-vs-mcp-choice** |

**Not** an MCP server Hello World ([anthropics mcp-builder](https://github.com/anthropics/skills) already covers that).  
This pack is **contract discipline for tools agents already call**.

---

## What you get (9 skills)

| When you… | Use |
|-----------|-----|
| Design a new tool / function schema | [`tool-contract-design`](skills/tool-contract-design/SKILL.md) |
| Changed tool JSON / MCP tools list | [`tool-schema-breaking-review`](skills/tool-schema-breaking-review/SKILL.md) |
| Writes under agent retry | [`tool-idempotency-and-retries`](skills/tool-idempotency-and-retries/SKILL.md) |
| Decide who may call what | [`tool-permission-matrix`](skills/tool-permission-matrix/SKILL.md) |
| Money / delete / prod changes | [`human-approval-gates`](skills/human-approval-gates/SKILL.md) |
| Audit an existing MCP | [`mcp-tool-surface-review`](skills/mcp-tool-surface-review/SKILL.md) |
| Skill vs MCP vs both | [`skill-vs-mcp-choice`](skills/skill-vs-mcp-choice/SKILL.md) |
| Prove tool-use quality | [`agent-tool-eval`](skills/agent-tool-eval/SKILL.md) |
| Not sure which skill | [`using-ai-surface-skills`](skills/using-ai-surface-skills/SKILL.md) |

Each skill: **triggers · steps · exit criteria · anti-patterns · output template**.

---

## Install options

| Method | How |
|--------|-----|
| **Claude user (recommended)** | `.\scripts\install.ps1 -Claude` |
| Project-local | `.\scripts\install.ps1 -Project` |
| Plugin | `/plugin marketplace add Wanbinyu/ai-surface-skills` |
| **Single skill only** | e.g. https://github.com/Wanbinyu/skill-tool-schema-breaking-review |

---

## Sister pack (HTTP for humans)

| Pack | Surface |
|------|---------|
| [api-platform-skills](https://github.com/Wanbinyu/api-platform-skills) | HTTP / OpenAPI |
| **This** | Tool / MCP for **agents** |

All solo skills: https://github.com/Wanbinyu?tab=repositories&q=skill-

---

## Not this pack

| Do | Don’t |
|----|--------|
| Tool contract evolution & safety | FastMCP / MCP SDK tutorials |
| Review existing MCP tool lists | Product “how to use Foo MCP” manuals |
| HITL + permissions | Red-team exploits |

Details: [docs/NOT-ANOTHER-MCP-BUILDER.md](docs/NOT-ANOTHER-MCP-BUILDER.md)

---

## Docs

| Doc | Purpose |
|-----|---------|
| [README.zh-CN.md](README.zh-CN.md) | 中文完整版 |
| [docs/DAY3-READY.md](docs/DAY3-READY.md) | Day3 social posts (copy-paste) |
| [docs/CLAUDE.md](docs/CLAUDE.md) | Claude install notes |
| [examples/toy-tools/](examples/toy-tools/) | v1 / v2-bad fixtures |

## License

MIT · [Wanbinyu](https://github.com/Wanbinyu)
