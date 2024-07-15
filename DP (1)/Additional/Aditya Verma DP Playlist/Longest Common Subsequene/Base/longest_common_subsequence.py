# A subsequence is defined as a sequence that can be derived from another string/sequence by deleting some or
# none of the elements without changing the order of the remaining elements.

# Properties of Subsequence:
# A sequence is a subsequence of itself.
# The empty sequence is a subsequence of every sequence.
# The number of possible subsequences of a sequence of length n is 2n.
# A subsequence of a subsequence is also a subsequence of the original sequence.
# The relative order of characters is unchanged.

# A longest common subsequence (LCS) is defined as the longest subsequence which is common in all given input sequences.

# s1 = “AGGTAB”, s2 = “GXTXAYB”, output will be 4 i.e GTAB


# Top - Bottom (Memoization)
def longest_common_subsequence(s1, s2, m, n, dp):
    if m == 0 or n == 0:
        return 0

    if dp[m][n] != 0:
        return dp[m][n]

    if s1[m - 1] == s2[n - 1]:
        dp[m][n] = 1 + longest_common_subsequence(s1, s2, m - 1, n - 1, dp)
    else:
        dp[m][n] = max(
            longest_common_subsequence(s1, s2, m, n - 1, dp),
            longest_common_subsequence(s1, s2, m - 1, n, dp),
        )
    return dp[m][n]


# Bottom - Up (Tabulation)
def longest_common_subsequence2(s1, s2, m, n):
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for row in range(1, m + 1):
        for col in range(1, n + 1):
            if s1[row - 1] == s2[col - 1]:
                dp[row][col] = 1 + dp[row - 1][col - 1]
            else:
                dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])
    return dp[m][n]


if __name__ == "__main__":
    s1 = "AGGTAB"
    s2 = "GXTXAYB"
    m, n = len(s1), len(s2)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    print(longest_common_subsequence(s1, s2, m, n, dp))
    print(longest_common_subsequence2(s1, s2, m, n))
