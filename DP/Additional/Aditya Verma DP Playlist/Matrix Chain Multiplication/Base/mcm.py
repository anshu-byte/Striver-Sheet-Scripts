def mcm(nums, i, j, dp):

    if i >= j:
        return 0

    if dp[i][j] != float("inf"):
        return dp[i][j]

    for k in range(i, j):
        temp = (
            mcm(nums, i, k, dp)
            + mcm(nums, k + 1, j, dp)
            + nums[i - 1] * nums[k] * nums[j]
        )

        dp[i][j] = min(temp, dp[i][j])
    return dp[i][j]


def mcm2(nums):
    n = len(nums)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    # Chain length varies from 2 to n-1
    for chain in range(2, n):
        for row in range(1, n - chain + 1):
            col = row + chain - 1
            dp[row][col] = float("inf")
            for k in range(row, col):
                temp = dp[row][k] + dp[k + 1][col] + nums[row - 1] * nums[k] * nums[col]
                dp[row][col] = min(temp, dp[row][col])
    return dp[1][n - 1]


if __name__ == "__main__":
    nums1 = [40, 20, 30, 10, 30]
    nums2 = [1, 2, 3, 4, 3]
    n1 = len(nums1)
    n2 = len(nums2)
    dp1 = [[float("inf") for _ in range(n1)] for _ in range(n1)]
    dp2 = [[float("inf") for _ in range(n2)] for _ in range(n2)]
    print(mcm(nums1, 1, n1 - 1, dp1))
    print(mcm(nums2, 1, n2 - 1, dp2))
    print(mcm2(nums1))
    print(mcm2(nums2))
