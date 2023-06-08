class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for col in range(n)]for row in range(m)]
        def fun(x,y):
            if x==m or y ==n:
                return 1
            if(dp[x][y]!=-1):
                return dp[x][y]
            dp[x][y] = fun(x+1,y) + fun(x,y+1)
            return dp[x][y]
        return fun(1,1)

sol = Solution()
print(sol.uniquePaths(23,12))