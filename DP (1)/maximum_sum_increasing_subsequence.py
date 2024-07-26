class Solution:
    def sumOfLIS(self, nums, prev_index, index, dp):
        if index == len(nums):
            return 0

        if dp[prev_index][index] != -1:
            return dp[prev_index][index]

        not_take = self.sumOfLIS(nums, prev_index, index + 1, dp)
        take = 0
        if nums[prev_index] < nums[index] or prev_index == -1:
            take = 1 + self.sumOfLIS(nums, index, index + 1, dp)
            return take

        dp[prev_index][index] = max(not_take, take)
        return dp[prev_index][index]


if __name__ == "__main__":
    nums = [1, 101, 2, 3, 100]
    n = len(nums)
    sol = Solution()
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    print(sol.sumOfLIS(nums, -1, 0, dp))
