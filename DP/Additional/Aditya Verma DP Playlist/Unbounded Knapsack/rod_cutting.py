class Solution:
    def cutRod(self, price, n):
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

        for row in range(1, n + 1):
            for col in range(1, n + 1):
                if row > col:
                    dp[row][col] = dp[row - 1][col]
                else:
                    dp[row][col] = max(
                        price[row - 1] + dp[row][col - row], dp[row - 1][col]
                    )
        return dp[n][n]


if __name__ == "__main__":
    price = [1, 5, 8, 9, 10, 17, 17, 20]
    price2 = [3, 5, 8, 9, 10, 17, 17, 20]
    sol = Solution()
    print(sol.cutRod(price, len(price)))
    print(sol.cutRod(price2, len(price2)))
