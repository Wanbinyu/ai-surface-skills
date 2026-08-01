# Claude / Claude Code

## Install to personal skills

```powershell
cd G:\skill\ai-surface-skills
.\scripts\install.ps1 -Claude
```

Path: `%USERPROFILE%\.claude\skills\<name>\`

Restart Claude Code, then try:

```text
对比 examples/toy-tools 的 tools.v1.json 和 tools.v2-bad.json，
用 tool-schema-breaking-review 出合并 verdict。
```

## Plugin

```text
/plugin marketplace add Wanbinyu/ai-surface-skills
/plugin install ai-surface-skills@ai-surface-skills
/reload-plugins
```

## Triggers (Chinese OK)

破坏性变更、tool 权限、人审、幂等重试、MCP 工具面审查、skill 还是 MCP
