# Day3 发布包（复制即发）

> **一句话：** 两套 Agent Skills 合集 + 19 个独立 skill 仓库 · MIT · 中英文档  
> 建议发出日：明天（文案已齐）

### 发帖前自检（30 秒）

1. 打开 https://github.com/Wanbinyu/ai-surface-skills — 顶部应有 Demo GIF  
2. 打开 https://github.com/Wanbinyu/api-platform-skills — 安装与试用提示词在最上方  

### 核心链接（置顶可复制）

| 项 | 链接 |
|----|------|
| Tool/MCP 合集 | https://github.com/Wanbinyu/ai-surface-skills |
| HTTP 合集 | https://github.com/Wanbinyu/api-platform-skills |
| 19 个独立 skill | https://github.com/Wanbinyu?tab=repositories&q=skill- |
| 爆款示例 skill | https://github.com/Wanbinyu/skill-breaking-change-review |

---

## 二、建议发出顺序（明天 30–60 分钟）

| 顺序 | 渠道 | 用哪段 | 预计时间 |
|------|------|--------|----------|
| 1 | 即刻 / 朋友圈 / 微博 / X | **§三 中文短帖** | 2 分钟 |
| 2 | V2EX（分享创造）或 掘金 | **§四 中文长帖** | 10 分钟 |
| 3 | Show HN **或** Reddit r/claudeai | **§五 英文** | 10 分钟 |
| 4 | （可选）awesome PR | **§六** | 10 分钟 |

不必四个都发；**至少完成 1 +（2 或 3）** 即算 Day3 达标。

发完后在本文件底部「完成打勾」里打勾。

---

## 三、中文短帖（即刻 / 朋友圈 / X）

### 版本 A（推荐）

```text
做了两套开源 Agent Skills，并拆成「一个 skill 一个仓库」：

1) HTTP 契约演进（破坏性变更、弃用、幂等、changelog…）
https://github.com/Wanbinyu/api-platform-skills

2) Tool/MCP 契约（tool 破坏性审查、权限、人审、评测…）
https://github.com/Wanbinyu/ai-surface-skills

不是又一个 REST 命名课，也不是 MCP Hello World。
19 个独立 skill：https://github.com/Wanbinyu?tab=repositories&q=skill-
```

### 版本 B（更短）

```text
Agent Skills 开源 Day3：HTTP 契约 + Tool/MCP 契约两套合集，
每个 skill 也可单独装。MIT · 中英文档。
合集：github.com/Wanbinyu/api-platform-skills
      github.com/Wanbinyu/ai-surface-skills
单 skill 示例：github.com/Wanbinyu/skill-breaking-change-review
```

---

## 四、中文长帖（V2EX / 掘金 / 知乎想法）

### 标题（任选）

1. `开源：给 Coding Agent 用的 API / Tool 契约 Skills（一个 skill 一个仓库）`
2. `不做又一个 api-design：HTTP 演进 + MCP Tool 表面纪律两套开源包`
3. `Claude / Codex 可装的 Agent Skills：破坏性变更、幂等、人审、Tool 评测`

### 正文

```text
背景
----
用 Claude Code / Codex / Cursor 改接口、接 MCP 时，模型很会「写代码」，
但经常：
- 默默 rename 字段 / tool 名
- POST 重试导致双写
- 给 agent 开了退款类 tool 却没有人审
- 装了一堆 MCP，不知道工具面是否安全

通用 skill 大礼包和 REST 命名教程已经很多了；
我们做的是「契约演进层」——上线后怎么不炸调用方、不炸 agent。


做了什么
--------
【合集 A】api-platform-skills
面向 HTTP / OpenAPI（给人与 SDK）
- 契约优先、兼容矩阵、破坏性变更审查
- 弃用剧本、CDC、幂等、Webhook
- API 安全表面、changelog
https://github.com/Wanbinyu/api-platform-skills

【合集 B】ai-surface-skills
面向 Tool / MCP / function calling（给 Agent）
- tool 契约设计、schema 破坏性审查
- 重试幂等、权限矩阵、人审门闸
- MCP 工具面审查、skill vs MCP 选型、tool 评测
https://github.com/Wanbinyu/ai-surface-skills
（不是 anthropics mcp-builder 那种「从零搭 MCP Server」）

【分发】一个 skill = 一个 GitHub 仓库
前缀 skill-，例如：
https://github.com/Wanbinyu/skill-breaking-change-review
https://github.com/Wanbinyu/skill-tool-schema-breaking-review
全部：https://github.com/Wanbinyu?tab=repositories&q=skill-

中英 README 并存；SKILL.md 以英文为主方便 agent 执行。


怎么装（Claude Code）
--------------------
# 整包
git clone https://github.com/Wanbinyu/ai-surface-skills.git
cd ai-surface-skills
.\scripts\install.ps1 -Claude

# 或只装一个
git clone https://github.com/Wanbinyu/skill-breaking-change-review.git
cd skill-breaking-change-review
.\scripts\install.ps1 -Claude

重启 Claude 后可试：
「对比 toy OpenAPI / toy tools 的 v1 与 v2-bad，按 breaking review 出报告」


欢迎
----
Star / Issue / PR 都欢迎。
定位是工程纪律包，不是 AI slop 大礼包。
MIT。
```

---

## 五、英文（Show HN / Reddit / X）

### Show HN

**Title:**

```text
Show HN: Agent skills for API and tool/MCP contracts (one skill per repo)
```

**Body:**

```text
I kept seeing coding agents rename fields/tools and ship silent breaks.

Two MIT skill packs (Claude Code / Codex / Cursor, Agent Skills format):

1) api-platform-skills — HTTP/OpenAPI evolution
   breaking-change review, deprecation, idempotency, webhooks, API surface security, changelog
   https://github.com/Wanbinyu/api-platform-skills

2) ai-surface-skills — tool/MCP surface discipline
   tool contract design, schema breaking review, permissions, human approval gates, MCP tool audit, tool-use eval
   https://github.com/Wanbinyu/ai-surface-skills
   (Not another MCP server scaffold — orthogonal to anthropics/mcp-builder)

Also published as 19 standalone repos (skill-*), bilingual README (EN + zh-CN).

Demo fixtures:
- bad OpenAPI upgrade → MERGE BLOCKED
- bad tools.v1 → tools.v2-bad → rename + required params + refund without HITL

Install: clone + scripts/install.ps1 -Claude (or install.sh --claude)

Feedback welcome.
```

### Reddit (r/claudeai 或 r/LocalLLaMA)

**Title:**

```text
Open-source Agent Skills: HTTP contract evolution + Tool/MCP surface (19 solo repos)
```

**Body:** 同 Show HN Body，可再加一句：

```text
Happy to take issues if a skill's exit criteria is too weak or conflicts with your harness.
```

### English short (X)

```text
HTTP contracts evolve. Tool contracts should too.

api-platform-skills + ai-surface-skills (MIT)
19 solo skill repos under skill-*

https://github.com/Wanbinyu/ai-surface-skills
https://github.com/Wanbinyu/api-platform-skills
```

---

## 六、（可选）Awesome 列表 PR

**目标仓示例：** https://github.com/VoltAgent/awesome-agent-skills  

**PR 标题：**

```text
Add api-platform-skills and ai-surface-skills (contract evolution packs)
```

**PR 描述 / 列表条目：**

```markdown
### API / Tool contracts
- [api-platform-skills](https://github.com/Wanbinyu/api-platform-skills) - HTTP/OpenAPI evolution: breaking changes, deprecation, idempotency, webhooks, API surface security, changelog
- [ai-surface-skills](https://github.com/Wanbinyu/ai-surface-skills) - Tool/MCP surface: contract design, schema breaking review, permissions, HITL, MCP tool audit, tool-use eval (not an MCP server builder)
```

开 PR 命令示例（需 fork 后）：

```powershell
# 按 awesome 仓 CONTRIBUTING 流程 fork → 改 README → PR
# 条目粘贴上面 markdown 即可
```

---

## 七、评论区备用回复

中文：

```text
谢谢！装完后可对 examples 里的 v1 / v2-bad 跑 breaking review。
单 skill 安装用 skill-* 仓库，整包用两个合集仓库。欢迎提 issue。
```

英文：

```text
Thanks! Try the toy fixtures under examples/ with the breaking-review skills.
Solo install: skill-* repos; bulk: the two collection repos. Issues welcome.
```

---

## 八、发帖后打勾（明天勾）

- [ ] 中文短帖已发  
- [ ] 中文长帖或英文长帖至少 1 个已发  
- [ ] （可选）awesome PR 已开  
- [ ] 帖子链接贴回本文件或记在别处  

### 帖子链接记录区

```text
短帖：
长帖：
英文：
awesome PR：
```

---

## 九、一句话定位（置顶 / 签名档）

```text
Agent Skills · HTTP 契约演进 + Tool/MCP 契约 · 一个 skill 一个仓库 · MIT
github.com/Wanbinyu/api-platform-skills · github.com/Wanbinyu/ai-surface-skills
```
