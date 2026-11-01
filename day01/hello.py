# Day 01 练习：环境自检脚本
# 目标：跑通这段代码，理解 Python 脚本不需要 main 方法、不需要 class 包裹

import sys
import platform


def greet(name: str) -> str:
    """返回问候语。注意是 return 不是 print —— print 只输出到屏幕，函数返回的是 None。"""
    return f"Hello, {name}!"


def main() -> None:
    print("=" * 40)
    print("Python 版本:", sys.version.split()[0])
    print("解释器路径:", sys.executable)
    print("操作系统:", platform.system(), platform.release())
    print("=" * 40)

    # 小练习 1：f-string 写法
    print(f"我的学习仓库跑通了，Python 版本 {sys.version.split()[0]}")

    # 小练习 2：列表推导式生成 1~10 的平方
    # 读法：对 range(1, 11) 里的每个 i，产出 i*i，组成列表
    print([i * i for i in range(1, 11)])

    # 小练习 3：调用 greet 并打印返回值（不 print 的话返回值就丢了）
    print(greet("xxx"))


# 这行相当于 Java 的 public static void main
if __name__ == "__main__":
    main()
