from subset_sum import subsetSum2
from typing import List


class Solution:
    # Bottom - Up (Tabulation)
    def subsetSum(self, nums, sum, n, dp):

        for row in range(n + 1):
            dp[row][0] = True

        # Traversal
        for row in range(1, n + 1):
            for col in range(1, sum + 1):
                if (
                    nums[row - 1] > col
                ):  # If row-1 th element is greater than sum, it cannot be included
                    dp[row][col] = dp[row - 1][col]
                else:
                    # Either Include or Exclude to get the desired sum
                    dp[row][col] = dp[row - 1][col - nums[row - 1]] or dp[row - 1][col]
        return dp[n][sum]

    def minimum_subset_sum_difference(self, nums):
        # Shifted negative values to positive
        min_num = min(nums)
        if min_num < 0:
            for i in range(len(nums)):
                nums[i] -= min_num
        total_sum = sum(nums)
        target = total_sum // 2

        # Initialization
        n = len(nums)
        dp = [[False for _ in range(target + 1)] for _ in range(n + 1)]

        self.subsetSum(nums, target, n, dp)

        for current_sum in range(target, -1, -1):
            if dp[n][current_sum]:  # last row of dp
                return total_sum - 2 * current_sum

        return -1

    def minimumDifference(self, nums: List[int]) -> int:
        return self.minimum_subset_sum_difference(nums)


def minimum_subset_sum_difference(nums):
    # Shifted negative values to positive
    min_num = min(nums)
    if min_num < 0:
        for i in range(len(nums)):
            nums[i] -= min_num
    total_sum = sum(nums)
    target = total_sum // 2

    for current_sum in range(target, -1, -1):
        if subsetSum2(nums, current_sum, len(nums)):
            return total_sum - 2 * current_sum

    return -1


if __name__ == "__main__":
    nums = [1, 6, 11, 5]  # [1,6,5] S1 and [11] S2
    nums2 = [1, 2, 7]  # [1,2] S1 and [7] S2
    nums3 = [-36, 36]
    nums4 = [1, 2, 3]

    print(minimum_subset_sum_difference(nums))
    print(minimum_subset_sum_difference(nums2))
    print(minimum_subset_sum_difference(nums3))
    print(minimum_subset_sum_difference(nums4))

    # reduced space complexity
    print()
    sol = Solution()
    print(sol.minimum_subset_sum_difference(nums))
    print(sol.minimum_subset_sum_difference(nums2))
    print(sol.minimum_subset_sum_difference(nums3))
    print(sol.minimum_subset_sum_difference(nums4))
