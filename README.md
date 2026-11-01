# ai-agent-study

Java 转 AI 应用开发的学习仓库。目标：2027-03 前具备 AI 应用 / Agent 开发能力。

## 目录

| 目录 | 内容 |
|---|---|
| `day01/` | Python 环境验证、f-string、列表推导式、函数返回值 |
| `day02/` | 变量 / 数据类型 / f-string 练习 |
| `notes/` | 每日学习笔记（Java ↔ Python 差异对照） |

## 环境

- Python 3.12（uv 托管，位于项目 `.venv`）
- uv 管理虚拟环境与依赖
- VS Code + Python 扩展 + Ruff

## 常用命令

```bash
uv venv                        # 创建虚拟环境
uv run python day01/hello.py   # 运行脚本（自动用项目环境，无需 activate）
uv add requests                # 添加依赖（写入 pyproject.toml）
uv sync                        # 按 pyproject.toml 同步依赖
```

## 密钥管理

`.env` 已被 `.gitignore` 忽略，参考 `.env.example` 创建本地 `.env`：

```
DEEPSEEK_API_KEY=sk-xxxxxxxx
```

**规则：密钥永不写进代码、永不提交到 Git。**
