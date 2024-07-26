class Solution:
    def is_palindrome(self, s, i, j, dp1):
        if i >= j:
            return True
        if dp1[i][j] != -1:
            return dp1[i][j]
        if s[i] == s[j]:
            dp1[i][j] = self.is_palindrome(s, i + 1, j - 1, dp1)
        else:
            dp1[i][j] = False
        return dp1[i][j]

    def helper(self, s, i, j, dp, dp1):
        if i >= j or self.is_palindrome(s, i, j, dp1):
            return 0

        if dp[i][j] != 0:
            return dp[i][j]

        res = float("inf")
        for k in range(i, j):
            temp = self.helper(s, i, k, dp, dp1) + self.helper(s, k + 1, j, dp, dp1) + 1
            res = min(res, temp)
        dp[i][j] = res
        return dp[i][j]

    def minCut(self, s: str) -> int:
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        dp1 = [[-1 for _ in range(len(s))] for _ in range(len(s))]
        return self.helper(s, 0, len(s) - 1, dp, dp1)


# passed 27/37 test cases leetcode
if __name__ == "__main__":
    sol = Solution()
    s = "geek"
    print(sol.minCut(s))
