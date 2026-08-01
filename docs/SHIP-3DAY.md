# 3 天分批上 GitHub 计划

本地项目：`G:\skill\ai-surface-skills`  
目标仓库：`https://github.com/Wanbinyu/ai-surface-skills`（公开 · MIT）

原则：**代码一次做完；公开分 3 天**，每天有可传播的增量，避免第一天丢半成品。

---

## Day 0（今天 · 本地完成 · 可不公开）

- [x] 仓库骨架 + 9 个 skill  
- [x] toy-tools 夹具 + sample reports  
- [x] install / validate / Claude plugin 清单  
- [x] README + 避撞文档 + 本文  
- [ ] `git init` + 本地 commit（不 push 或 push 但保持 private 亦可）

```powershell
cd G:\skill\ai-surface-skills
python scripts\validate_skills.py
.\scripts\install.ps1 -Claude
```

---

## Day 1 — 公开仓库 + 最小可用

**目标：** 链接可分享，别人能 clone 安装。

| 动作 | 说明 |
|------|------|
| 创建公开 repo | `gh repo create Wanbinyu/ai-surface-skills --public --source=. --remote=origin --push` |
| Topics | `agent-skills` `mcp` `claude-code` `codex` `tools` `function-calling` |
| Tag | `v0.1.0-rc1` 或直接 `v0.1.0` |
| 自测 | Claude 跑 toy-tools breaking review |

**发帖（轻量）：** 仅发仓库链接 + 一句话定位（中文短帖即可）。  
文案见 [SOCIAL.md](SOCIAL.md) Day1 段。

---

## Day 2 — Demo + 可信度

**目标：** README 有 demo，金标准可对照。

| 动作 | 说明 |
|------|------|
| 确认 sample-reports 与 agent 输出一致 | 微调 skill 若有漏报 |
| （可选）录 GIF / 终端录像 | 参考 api-platform-skills demo |
| 补 Release notes | GitHub Release 写清「不是 mcp-builder」 |
| 二次传播 | 回复评论、中英各一帖 |

---

## Day 3 — 生态曝光

**目标：** 被索引、被装。

| 动作 | 说明 |
|------|------|
| Show HN / Reddit / V2EX / 即刻 选 1–2 | 用 SOCIAL Day3 长文 |
| PR 到 awesome-agent-skills（若接受） | VoltAgent 等列表 |
| 与 api-platform-skills README 互链 | 系列双包 |
| Tag `v0.1.0` final（若 Day1 用了 rc） | |

---

## 时间表示例

| 日 | 日期占位 | 对外 |
|----|----------|------|
| Day 0 | 本地完成日 | 不强制公开 |
| Day 1 | +1 | **public push** |
| Day 2 | +2 | demo / release 打磨 |
| Day 3 | +3 | 社区帖 |

（把占位换成你的真实日历即可。）

---

## Day 1 一键命令（到时执行）

```powershell
cd G:\skill\ai-surface-skills
python scripts\validate_skills.py
git add -A
git status
# 配置好 user.name / user.email 后：
git commit -m "feat: AI Surface Skills v0.1.0 — tool/MCP contract pack"
git branch -M main
gh repo create ai-surface-skills --public --source=. --remote=origin --description "Agent skills for tool/MCP contracts — evolution, permissions, HITL, eval. Not another MCP builder." --push
gh repo edit Wanbinyu/ai-surface-skills --add-topic agent-skills --add-topic mcp --add-topic claude-code --add-topic tools --add-topic function-calling
git tag -a v0.1.0 -m "v0.1.0"
git push origin v0.1.0
```

---

## 完成定义

| 日 | Done when |
|----|-----------|
| Day 1 | 公开 URL 可 clone，`install.ps1 -Claude` 可用 |
| Day 2 | 至少 1 个 demo 证据 + Release 说明 |
| Day 3 | 至少 1 个公开社区帖发出 |

## Day1 executed

- Public: https://github.com/Wanbinyu/ai-surface-skills
- Visibility: PUBLIC
- Tag/Release: v0.1.0
- Topics: agent-skills, mcp, claude-code, tools, function-calling, codex, skills

Next: Day2 demo polish (optional GIF), Day3 community posts (docs/SOCIAL.md).
