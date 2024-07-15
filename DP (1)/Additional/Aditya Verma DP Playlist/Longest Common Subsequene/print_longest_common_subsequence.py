def print_longest_common_subsequence(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    i, j = m, n
    res = ""
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            res += s1[i - 1]
            i -= 1
            j -= 1
        else:
            if dp[i][j - 1] > dp[i - 1][j]:
                j -= 1
            else:
                i -= 1
    reverse_res = res[::-1]
    return reverse_res


if __name__ == "__main__":
    s1 = "acbcf"
    s2 = "abcdaf"
    print(print_longest_common_subsequence(s1, s2))
