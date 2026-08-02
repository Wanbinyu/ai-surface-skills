# AI Surface Skills

[English](README.md) | **中文**

<p align="center">
  <strong>别再让 Agent 乱用 Tool / MCP。</strong><br/>
  <em>HTTP 契约会演进，Tool 契约也该如此。</em>
</p>

---

## 先做这两步（约 1 分钟）

### 1. 安装（Claude Code）

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

重启 Claude Code。技能进入 `~/.claude/skills/`。

### 2. 立刻试这条提示词

```text
对比 examples/toy-tools/tools.v1.json 和 tools.v2-bad.json，
按 tool-schema-breaking-review 出合并 verdict，
并对 v2-bad 标权限风险。
```

**正常结果：** `request-changes`——tool 改名、参数变必填、列表描述越权、`refund_order` 无人审。

Demo GIF 见 [README.md](README.md) 顶部。

---

## 解决什么问题

| 痛点 | 对应 skill |
|------|------------|
| Agent 改 tool 名，旧 prompt 全挂 | **tool-schema-breaking-review** |
| 超时重试导致双下单 | **tool-idempotency-and-retries** |
| 退款/删除类 tool 默认可用 | **tool-permission-matrix** + **human-approval-gates** |
| 装了第三方 MCP 不知是否安全 | **mcp-tool-surface-review** |
| 该做 skill 还是 MCP | **skill-vs-mcp-choice** |

**不是** MCP Server 从零搭建教程（官方 mcp-builder 已有）。  
本包管的是：**Agent 已经能调用的 tool 面，如何设计、演进、授权、人审、评测。**

---

## 你得到什么（9 个 skill）

| 场景 | 用 |
|------|-----|
| 设计新 tool / function schema | `tool-contract-design` |
| 改了 tool JSON / MCP 列表 | `tool-schema-breaking-review` |
| 有副作用 + 会重试 | `tool-idempotency-and-retries` |
| 谁能调什么 | `tool-permission-matrix` |
| 涉及钱/删数据/改生产 | `human-approval-gates` |
| 审查已有 MCP | `mcp-tool-surface-review` |
| skill 还是 MCP | `skill-vs-mcp-choice` |
| tool 调用质量回归 | `agent-tool-eval` |
| 不知道用哪个 | `using-ai-surface-skills` |

每个 skill：**触发条件 · 步骤 · 完成标准 · 反模式 · 输出模板**。

---

## 安装方式

| 方式 | 做法 |
|------|------|
| **推荐：Claude 全局** | `.\scripts\install.ps1 -Claude` |
| 仅当前项目 | `-Project` |
| 插件 | `/plugin marketplace add Wanbinyu/ai-surface-skills` |
| **只要一个 skill** | 例：https://github.com/Wanbinyu/skill-tool-schema-breaking-review |

---

## 姊妹包

| 包 | 对象 |
|----|------|
| [api-platform-skills](https://github.com/Wanbinyu/api-platform-skills) | HTTP / OpenAPI |
| **本包** | Tool / MCP → **Agent** |

全部独立 skill：https://github.com/Wanbinyu?tab=repositories&q=skill-

---

## 明确不做

- FastMCP / MCP SDK Hello World  
- 某个产品的「如何使用 XXX MCP」说明书  
- 红队 exploit  

详见：[docs/NOT-ANOTHER-MCP-BUILDER.md](docs/NOT-ANOTHER-MCP-BUILDER.md)

## 许可证

MIT · [Wanbinyu](https://github.com/Wanbinyu)
