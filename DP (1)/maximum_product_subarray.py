from typing import List


def maxProduct(nums: List[int]) -> int:
    pre, suff = 1, 1
    res = float("-inf")
    n = len(nums)
    for i in range(n):
        if pre == 0:
            pre = 1
        if suff == 0:
            suff = 1
        pre *= nums[i]
        suff *= nums[n - 1 - i]

        res = max(res, max(pre, suff))
    return res


if __name__ == "__main__":
    nums = [2, 3, -2, 4]
    print(maxProduct(nums))
