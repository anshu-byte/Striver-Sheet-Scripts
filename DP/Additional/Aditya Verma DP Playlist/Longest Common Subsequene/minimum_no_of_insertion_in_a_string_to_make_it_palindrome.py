from Base.longest_common_subsequence import longest_common_subsequence2


def longest_palindromic_subsequence(s):
    s1, s2 = s, s[::-1]
    n = len(s)
    return longest_common_subsequence2(s1, s2, n, n)


if __name__ == "__main__":
    s = "aebcbda"
    print(
        "No. of insertion / No.of deletion", len(s) - longest_palindromic_subsequence(s)
    )
