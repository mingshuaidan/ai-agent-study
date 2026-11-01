# Day 02 练习题：变量 / 数据类型 / f-string

> 目标：把 Java 的类型思维切换成 Python 思维。做完这 10 题，明天上午就能进"列表/字典"。
> 在 `exercise.py` 里写，每题一个函数或一段代码，写完跑 `uv run python day02/exercise.py` 验证。

## 一、基础（必做，8 题）

**1. 变量声明对比**
定义一个 `age = 25`、`name = "张三"`、`height = 1.75`、`is_student = True`，然后**不写类型**地打印它们。思考：为什么 Python 不用写 `int age = 25`？

**2. 动态类型**
先 `x = 100`，打印 `type(x)`；再 `x = "一百"`，再打印 `type(x)`。思考：这和 Java 的强类型有什么不同？代价是什么？

**3. f-string 三种写法**
用三种方式输出"我叫张三，今年 25 岁"：
- `+` 拼接（记得 `str()` 转换）
- `%` 格式化（老写法，知道就行）
- **f-string**（推荐）
比较代码长短。

**4. f-string 表达式**
用 f-string 直接算：`print(f"一年后有 {age + 1} 岁")`、`print(f"身高保留一位小数：{height:.1f}")`。
再试：`print(f"{name!r}")` 和 `print(f"{age:>5}")`（了解格式化规格）。

**5. 数字类型**
`10 / 3`、`10 // 3`、`10 % 3`、`2 ** 10` 分别是什么？
注意：`/` 永远返回 **float**（Java 里 `int/int` 是整除，Python 不是！）。

**6. 类型转换**
`int("42")`、`float("3.14")`、`str(100)`、`int(3.9)`（会截断还是四舍五入？实测）。
再试 `int("3.14")` 会怎样？——体会 Python 的"报错文化"。

**7. 字符串方法**
给定 `s = "  Hello Python  "`，依次做：
- 去空格 `strip()`
- 转大写/小写 `upper()` / `lower()`
- 替换 `replace("Python", "AI")`
- 分割 `split(" ")`
- 判断开头 `startswith("He")`
- 查长度 `len(s)`

**8. None 与真假值**
- Python 的 `None` 对应 Java 的什么？判断用什么写法（`is None` 还是 `== None`）？
- 测一下：`bool(0)`、`bool("")`、`bool([])`、`bool("0")` 分别是什么？为什么 `bool("0")` 是 True？

## 二、进阶（选做，2 题）

**9. 多重赋值与交换**
```python
a, b = 1, 2
a, b = b, a   # 一行交换，Java 需要临时变量
```
再试 `x = y = z = 0`。想想原理（元组解包）。

**10. 输入处理**
用 `input()` 读用户输入（一定返回 str！），转成 int 后判断奇偶。思考：Java 的 `Scanner.nextInt()` 和它差在哪？

---

## 交付要求

- 代码写在 `day02/exercise.py`
- 每题上方用注释写题号
- 至少 3 处写"Java 对照"注释（例如：`# Java: int a = 10;`）
- 完成后跑通，输出无报错
