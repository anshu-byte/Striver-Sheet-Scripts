from Base.longest_common_subsequence import longest_common_subsequence2


def minimum_no_of_deletions_required_to_make_a_string_palindrome(s):
    s1, s2 = s, s[::-1]
    n = len(s)
    return n - longest_common_subsequence2(s1, s2, n, n)


if __name__ == "__main__":
    s = "agbcba"
    print(minimum_no_of_deletions_required_to_make_a_string_palindrome(s))
