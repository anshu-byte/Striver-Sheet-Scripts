# Top - Down (Memoization)
def knapsack(weights, values, capacity, n, dp):
    # no item left or capacity is 0
    if n == 0 or capacity == 0:
        return 0

    if dp[n][capacity] != -1:
        return dp[n][capacity]

    # If the weight of the nth item is more than the capacity, it cannot be included
    if weights[n - 1] > capacity:
        dp[n][capacity] = knapsack(weights, values, capacity, n - 1, dp)

    else:
        # Store the maximum of two cases:
        # (1) nth item included
        # (2) not included
        dp[n][capacity] = max(
            values[n - 1]
            + knapsack(weights, values, capacity - weights[n - 1], n - 1, dp),
            knapsack(weights, values, capacity, n - 1, dp),
        )

    return dp[n][capacity]


# Bottom - Up (Tabulation)
def knapsack2(weights, values, capacity, n):
    # Initialization
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Traversal
    for row in range(1, n + 1):
        for col in range(1, capacity + 1):
            # If the weight of the row-1 th item is more than the capacity, it cannot be included
            if weights[row - 1] > col:
                dp[row][col] = dp[row - 1][col]
            else:
                # Store the maximum of two cases:
                # (1) nth item included
                # (2) not included
                dp[row][col] = max(
                    values[row - 1] + dp[row - 1][col - weights[row - 1]],
                    dp[row - 1][col],
                )

    return dp[n][capacity]


weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 7
n = len(weights)

dp = [[-1 for _ in range(capacity + 1)] for _ in range(n + 1)]
max_value = knapsack(weights, values, capacity, n, dp)
print(f"The maximum value that can be obtained is: {max_value}")

max_value = knapsack2(weights, values, capacity, n)
print(f"The maximum value that can be obtained is: {max_value}")
