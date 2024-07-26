class Solution:

    # Brute Force
    def lengthOfLIS(self, nums):
        def is_increasing(subseq):
            for i in range(len(subseq) - 1):
                if subseq[i] >= subseq[i + 1]:
                    return False
            return True

        def generateAllSubsequences(index, subseq):
            if index == len(nums):
                if is_increasing(subseq):
                    nonlocal max_len
                    max_len = max(max_len, len(subseq))
                return
            generateAllSubsequences(index + 1, subseq)
            generateAllSubsequences(index + 1, subseq + [nums[index]])

        max_len = 0
        generateAllSubsequences(0, [])
        return max_len

    def lengthOfLIS2(self, nums):
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        return max(dp)

    def recursive_longest_common_subsequence(self, s1, s2, m, n):
        if m == 0 or n == 0:
            return 0

        if s1[m - 1] == s2[n - 1]:
            return 1 + self.recursive_longest_common_subsequence(s1, s2, m - 1, n - 1)
        else:
            return max(
                self.recursive_longest_common_subsequence(s1, s2, m, n - 1),
                self.recursive_longest_common_subsequence(s1, s2, m - 1, n),
            )

    def lengthOfLIS3(self, nums, prev_index, index):
        if index == len(nums):
            return 0
        not_take = self.lengthOfLIS3(nums, prev_index, index + 1)
        take = 0
        if nums[prev_index] < nums[index] or prev_index == -1:
            take = 1 + self.lengthOfLIS3(nums, index, index + 1)
            return take

        return max(not_take, take)

    def get_longest_increasing_subsequence_length(self, arr, n, ind, prev_index, dp):
        if ind == n:
            return 0

        if dp[ind][prev_index + 1] != -1:
            return dp[ind][prev_index + 1]

        not_take = 0 + self.get_longest_increasing_subsequence_length(
            arr, n, ind + 1, prev_index, dp
        )

        take = 0

        if prev_index == -1 or arr[ind] > arr[prev_index]:
            take = 1 + self.get_longest_increasing_subsequence_length(
                arr, n, ind + 1, ind, dp
            )

        dp[ind][prev_index + 1] = max(not_take, take)
        return dp[ind][prev_index + 1]


if __name__ == "__main__":
    nums = [0, 1, 0, 3]
    sol = Solution()
    print(sol.lengthOfLIS(nums))
    print(sol.lengthOfLIS2(nums))
    print(sol.lengthOfLIS3(nums, -1, 0))
    n = len(nums)
    dp = [[-1 for _ in range(n + 1)] for _ in range(n)]
    print(sol.get_longest_increasing_subsequence_length(nums, n, 0, -1, dp))
