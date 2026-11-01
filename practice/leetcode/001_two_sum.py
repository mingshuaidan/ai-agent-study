# LeetCode 1. 两数之和（简单）
# 题目：给定整数数组 nums 和整数 target，返回和为 target 的两个数的下标。
# 示例：nums = [2, 7, 11, 15], target = 9  ->  返回 [0, 1]
# 约束：每种输入只会对应一个答案，同一个元素不能重复使用。


def two_sum_brute(nums: list[int], target: int) -> list[int]:
    """暴力解法：双层循环。时间复杂度 O(n^2)，空间 O(1)。

    思路：
      外层 i 从头到尾，内层 j 从 i+1 开始（保证不重复使用同一元素），
      判断 nums[i] + nums[j] == target，成立就返回 [i, j]。
    """
    # TODO: 你来写（提醒：range(len(nums)) 拿索引；内层从 i + 1 开始）
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]
        


def two_sum_hash(nums: list[int], target: int) -> list[int]:
    """进阶解法：字典记录"值 -> 下标"，一遍循环。时间 O(n)，空间 O(n)。

    TODO: 明天学完字典再回来写。提示：遍历到 x 时，先看 target - x 在不在字典里。
    """
    # TODO


if __name__ == "__main__":
    # 三个测试用例，改完直接跑：uv run python practice/leetcode/001_two_sum.py
    print(two_sum_brute([2, 7, 11, 15], 9))    # 期望 [0, 1]
    print(two_sum_brute([3, 2, 4], 6))         # 期望 [1, 2]
    print(two_sum_brute([3, 3], 6))            # 期望 [0, 1]
