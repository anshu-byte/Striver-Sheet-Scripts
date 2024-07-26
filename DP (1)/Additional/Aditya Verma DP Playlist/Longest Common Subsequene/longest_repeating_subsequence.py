def longest_repeating_subsequence(s1, s2, m, n, dp):
    if m == 0 or n == 0:
        return 0

    if dp[m][n] != 0:
        return dp[m][n]

    if s1[m - 1] == s2[n - 1] and m != n:
        dp[m][n] = 1 + longest_repeating_subsequence(s1, s2, m - 1, n - 1, dp)
    else:
        dp[m][n] = max(
            longest_repeating_subsequence(s1, s2, m, n - 1, dp),
            longest_repeating_subsequence(s1, s2, m - 1, n, dp),
        )
    return dp[m][n]


def longest_repeating_subsequence2(s1, s2, m, n):
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for row in range(1, m + 1):
        for col in range(1, n + 1):
            if s1[row - 1] == s2[col - 1] and row != col:
                dp[row][col] = 1 + dp[row - 1][col - 1]
            else:
                dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])
    return dp[m][n]


if __name__ == "__main__":
    s = "aabebcdd"
    # s = "aba"
    n = len(s)
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    print(longest_repeating_subsequence(s, s, n, n, dp))
    print(longest_repeating_subsequence2(s, s, n, n))
