from Base.longest_common_subsequence import longest_common_subsequence2


def super_seq(X, Y, m, n):
    if not m:
        return n
    if not n:
        return m

    if X[m - 1] == Y[n - 1]:
        return 1 + super_seq(X, Y, m - 1, n - 1)

    return 1 + min(super_seq(X, Y, m - 1, n), super_seq(X, Y, m, n - 1))


# A supersequence is defined as the string which contains both the strings S1 and S2 as subsequences.
def print_shortest_common_supersequence(s1, s2, m, n):
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for row in range(m + 1):
        for col in range(n + 1):
            if row == 0:
                dp[row][col] = col
            elif col == 0:
                dp[row][col] = row
            elif s1[row - 1] == s2[col - 1]:
                dp[row][col] = 1 + dp[row - 1][col - 1]
            else:
                dp[row][col] = 1 + min(dp[row - 1][col], dp[row][col - 1])

    i, j = m, n
    res = ""
    while i > 0 and j > 0:

        if s1[i - 1] == s2[j - 1]:
            res = s1[i - 1] + res
            i -= 1
            j -= 1
        else:
            if dp[i - 1][j] > dp[i][j - 1]:
                res = s2[col - 1] + res
                j -= 1
            else:
                res = s1[i - 1] + res
                i -= 1

    while i > 0:
        res = s1[i - 1] + res
        i -= 1

    while j > 0:
        res = s2[j - 1] + res
        j -= 1
    return res


if __name__ == "__main__":
    s1 = "geek"
    s2 = "eke"
    m, n = len(s1), len(s2)
    print(super_seq(s1, s2, m, n))
    print(print_shortest_common_supersequence(s1, s2, m, n))
    # print(shortest_common_supersequence(s1, s2))
