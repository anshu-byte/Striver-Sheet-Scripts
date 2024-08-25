# A substring is defined as a contiguous part of a string, i.e., a string inside another string.

# A substring is a sequence of consecutive characters of a larger string or sequence whereas,
# in a subsequence, the characters need not to be consecutive.

# Properties of Subsequence:
# Starting position of a substring is greater than or equal to the starting index of the string and the ending position is less than or equal to the final position.
# The maximum length of a substring can be at most the same as the length of the string.
# In a substring, contiguous characters from the string are kept.
# The total possible number of substrings for a string of length n is (n*(n+1)/2)


def longest_common_substring(s1, s2, m, n):
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    res = 0
    for row in range(1, m + 1):
        for col in range(1, n + 1):
            if s1[row - 1] == s2[col - 1]:
                dp[row][col] = 1 + dp[row - 1][col - 1]
                res = max(res, dp[row][col])
            else:
                dp[row][col] = 0
    return res


if __name__ == "__main__":
    s1 = "abfce"
    s2 = "cdgab"
    m, n = len(s1), len(s2)
    print(longest_common_substring(s1, s2, m, n))
