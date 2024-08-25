from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        no_of_coins = len(coins)
        dp = [[0 for _ in range(amount + 1)] for _ in range(no_of_coins + 1)]

        for row in range(no_of_coins + 1):
            dp[row][0] = 1

        for row in range(1, no_of_coins + 1):
            for col in range(1, amount + 1):
                if coins[row - 1] > col:
                    dp[row][col] = dp[row - 1][col]
                else:
                    dp[row][col] = dp[row][col - coins[row - 1]] + dp[row - 1][col]
        return dp[no_of_coins][amount]


if __name__ == "__main__":
    coins = [1, 2, 3]
    amount = 5
    sol = Solution()
    print(sol.change(amount, coins))
