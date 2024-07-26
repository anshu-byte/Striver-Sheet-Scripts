class Solution:
    def edit_distance(self, s1, s2, m, n, dp):
        if m == 0 or n == 0:
            return max(m, n)
        if dp[m][n] != -1:
            return dp[m][n]

        if s1[m - 1] == s2[n - 1]:
            dp[m][n] = self.edit_distance(s1, s2, m - 1, n - 1, dp)
        else:
            del_op = 1 + self.edit_distance(s1, s2, m - 1, n, dp)
            ins_op = 1 + self.edit_distance(s1, s2, m, n - 1, dp)
            rep_op = 1 + self.edit_distance(s1, s2, m - 1, n - 1, dp)
            dp[m][n] = min(del_op, ins_op, rep_op)
        return dp[m][n]

    def minDistance(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        dp = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
        return self.edit_distance(s1, s2, m, n, dp)


if __name__ == "__main__":
    sol = Solution()
    s1 = "horse"
    s2 = "ros"
    m, n = len(s1), len(s2)
    dp = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
    print(sol.edit_distance(s1, s2, m, n, dp))
