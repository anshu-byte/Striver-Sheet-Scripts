from typing import List


class Solution:

    def coinChangeRecursive(self, coins, amount, n, count):
        if n == 0 and amount == 0:
            return count

        if n < 0:
            return float("inf")

        if coins[n - 1] > amount:
            return self.coinChangeRecursive(coins, amount, n - 1, count)
        else:
            return min(
                self.coinChangeRecursive(coins, amount - coins[n - 1], n, count + 1),
                self.coinChangeRecursive(coins, amount, n - 1, count),
            )

    def coinChange(self, coins, amount, n, dp):
        if n == 0 and amount == 0:
            return 0

        if n < 0:
            return float("inf")

        if dp[n][amount] != -1:
            return dp[n][amount]

        if coins[n - 1] > amount:
            dp[n][amount] = self.coinChange(coins, amount, n - 1, dp)
        else:
            dp[n][amount] = min(
                1 + self.coinChange(coins, amount - coins[n - 1], n, dp),
                self.coinChange(coins, amount, n - 1, dp),
            )
        return dp[n][amount]

    def coinChange2(self, coins, amount):
        n = len(coins)
        dp = [[float("inf")] * (amount + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 0

        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                if coins[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = min(dp[i][j - coins[i - 1]] + 1, dp[i - 1][j])

        return dp[n][amount] if dp[n][amount] != float("inf") else -1


if __name__ == "__main__":
    coins = [1, 2, 3]
    # coins = [2, 5, 10, 1]
    amount = 5
    # amount = 27
    n = len(coins)
    sol = Solution()
    dp = [[-1 for _ in range(amount + 1)] for _ in range(n + 1)]
    print(sol.coinChangeRecursive(coins, amount, n, 0))
    print(sol.coinChange(coins, amount, n, dp))
    print(sol.coinChange2(coins, amount))
