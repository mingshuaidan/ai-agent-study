# Day 01 笔记 - 2026-11-01（周日）

## 一、今日成果

- [x] Python 3.12.13（uv 托管）+ uv 0.11.19 + Git 2.55 环境就绪
- [x] 项目落地 `D:\ai-agent-study`（C 盘空间紧张，全部迁 D 盘）
- [x] VS Code + Python(Microsoft) + Ruff 扩展，解释器指向 `.venv`
- [x] `day01/hello.py` 跑通，3 道练习完成
- [ ] DeepSeek API Key 注册（待本人手机号验证）
- [ ] GitHub 首次 push（待账号与远程仓库）

## 二、环境信息

| 项 | 值 |
|---|---|
| Python | 3.12.13（`.venv` 内） |
| uv | 0.11.19 |
| Git | 2.55.0.windows.3 |
| 项目路径 | `D:\ai-agent-study` |
| 运行命令 | `uv run python day01/hello.py` |

## 三、踩坑记录（每条都有价值）

1. **Python 不用单独装**：机器上已有 uv 托管的 Python，直接 `uv python install 3.12` + `uv venv --python 3.12` 即可。uv 相当于 Python 界的 Maven + JDK 管理器。
2. **`uv run` 不需要 activate**：它会自动使用项目 `.venv`，绕开了 PowerShell 的 `ExecutionPolicy` 报错（`Activate.ps1 cannot be loaded`）。
3. **VS Code 选解释器要看清单里的路径**：`~\.venv`（C 盘用户目录）和 `.\.venv`（当前工程，D 盘）长得一样，选错就跑错环境。带 **Workspace** 标签的才是当前工程。
4. **用户级 settings.json 会压过工程配置**：`C:\Users\Lenovo\AppData\Roaming\Code\User\settings.json` 里硬编码了旧解释器路径，是黄波浪线的真正根因。
5. **Pylance 的黄波浪线是"显示问题"**：`import sys` 标黄 ≠ 代码错，`uv run` 走的是真实环境，输出正确即可。

## 四、Java ↔ Python 差异（今天学到的）

| 维度 | Java | Python |
|---|---|---|
| 入口 | `public static void main` | `if __name__ == "__main__":` |
| 类型 | 必须声明 `int age = 25` | 直接 `age = 25`，动态类型 |
| 字符串拼接 | `"a" + b`（需 `String.valueOf`） | `f"a{b}"`（f-string） |
| 循环造列表 | `Stream.rangeClosed(1,10).map(...).collect()` | `[i*i for i in range(1,11)]` |
| 输出 vs 返回 | `System.out.println` / `return` | `print()` / `return`（**不能混**） |
| 代码块 | 大括号 `{}` | **缩进**（4 个空格，硬规矩） |
| 类型注解 | 强类型，编译期检查 | `name: str` 只是提示，运行不强制 |

## 五、今天的三个坑（自我提醒）

1. **列表推导式不是可选项**：写成 `for + append` 等于白学 Python，会在后面处理数据时慢十倍。
2. **`print` 不是 `return`**：函数要"给"结果用 `return`，用 `print` 只是打屏，函数实际返回 `None`。
3. **`range(1, 11)` 不含 11**：左闭右开，这是 Python 切片体系的统一规则。

## 六、下一步

- 明日（11.2）：变量/数据类型/f-string 10 题 → `day02/exercise.py`
- 欠账：DeepSeek API Key、GitHub 建仓 push、LeetCode 1 题 + Java 八股
