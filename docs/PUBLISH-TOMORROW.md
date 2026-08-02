# 明天发布清单（Day2 + Day3）

> **代码与文案今天已备好；对外发帖 / 二次传播放在明天。**  
> Day1 仓库已公开：https://github.com/Wanbinyu/ai-surface-skills

日期约定（按你的「明天」）：

| 阶段 | 状态 |
|------|------|
| Day0 本地 | 已完成 |
| Day1 公开仓库 | **已完成**（今天） |
| **Day2 Demo 可信度** | **内容已就绪 → 明天对外强调** |
| **Day3 社区曝光** | **文案已就绪 → 明天发帖** |

---

## 明天上午 · Day2（约 30–45 分钟）

### 1. 自测（必做）

```powershell
cd G:\skill\ai-surface-skills
.\scripts\install.ps1 -Claude
# 重启 Claude Code 后发送：
```

```text
对比 examples/toy-tools/tools.v1.json 与 tools.v2-bad.json，
按 tool-schema-breaking-review 出报告，对照
examples/sample-reports/tool-breaking-v1-vs-v2-bad.md。
```

### 2. 确认 README Demo

- GIF：`assets/demo-tool-break.gif`（已生成）
- Poster：`assets/demo-poster.png`
- 浏览器打开仓库首页，确认 GIF 能显示

### 3. 轻量传播（Day2 短帖）

中文：

```text
AI Surface Skills 补了 Demo：tool 破坏性变更审查会挡住 rename / 必填收紧 / 无 HITL 退款工具。
不是 MCP 脚手架教程。
https://github.com/Wanbinyu/ai-surface-skills
```

English:

```text
Demo up: tool-schema-breaking-review blocks bad agent tool surfaces
(renames, required params, refund without HITL).
Not another MCP builder.
https://github.com/Wanbinyu/ai-surface-skills
```

### 4. （可选）更新 Release 说明

若要在 Release 里加 Demo 段落：

```powershell
gh release edit v0.1.0 --notes-file docs/RELEASE-v0.1.0.md
```

---

## 明天下午 · Day3（约 45–60 分钟）

### 1. 发 1–2 个社区帖（复制即用）

完整文案：[`SOCIAL.md`](SOCIAL.md)

推荐组合（任选 2）：

| 渠道 | 用哪段 |
|------|--------|
| 即刻 / 朋友圈 / X | SOCIAL Day1 短帖 或 上面 Day2 短帖 |
| V2EX / 掘金 / Show HN | SOCIAL Day3 长文 |
| Reddit r/claudeai | Day3 英文长文 |

### 2. 系列互链已就绪

- ai-surface README → api-platform  
- api-platform README → ai-surface  

发帖时可写：

```text
系列：
- HTTP 契约演进 https://github.com/Wanbinyu/api-platform-skills
- Agent Tool/MCP 契约 https://github.com/Wanbinyu/ai-surface-skills
```

### 3. （可选）awesome 列表

到 [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) 开 PR，描述用：

```text
## AI Surface / Tool contracts
- [ai-surface-skills](https://github.com/Wanbinyu/ai-surface-skills) — Tool/MCP contract evolution: breaking review, permissions, HITL, eval (not mcp-builder)
```

### 4. Day3 完成打勾

- [ ] 至少 1 个公开社区帖已发出  
- [ ] 帖内含仓库链接  
- [ ] （可选）awesome PR 已开  

---

## 今天不要做

- 不必再改大量 skill 内容（除非自测发现硬伤）  
- **不必今晚发社区长帖**（留给明天 Day2+Day3）  

---

## 一键自检（明天发帖前）

```powershell
cd G:\skill\ai-surface-skills
python scripts\validate_skills.py
git status
# 应与 origin/main 同步
git pull
gh repo view Wanbinyu/ai-surface-skills --json url,visibility
```


## Day2 done (2026-08-02)

- Monorepo demo/release confirmed.
- Solo skill GitHub publish batch started/finished this day.

