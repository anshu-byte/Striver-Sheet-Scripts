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


# Top - Down Approach
def recursive_longest_common_subsequence(s1, s2, m, n):
    if m == 0 or n == 0:
        return 0

    if s1[m - 1] == s2[n - 1]:
        return 1 + recursive_longest_common_subsequence(s1, s2, m - 1, n - 1)
    else:
        return max(
            recursive_longest_common_subsequence(s1, s2, m, n - 1),
            recursive_longest_common_subsequence(s1, s2, m - 1, n),
        )


# Bottom - Up Approach
def recursive_longest_common_subsequence2(s1, s2, index1, index2):
    if index1 == len(s1) or index2 == len(s2):
        return 0

    if s1[index1] == s2[index2]:
        index1 += 1
        index2 += 1
        return 1 + recursive_longest_common_subsequence2(s1, s2, index1, index2)
    else:
        return max(
            recursive_longest_common_subsequence2(s1, s2, index1 + 1, index2),
            recursive_longest_common_subsequence2(s1, s2, index1, index2 + 1),
        )


if __name__ == "__main__":
    s1 = "AGGTAB"
    s2 = "GXTXAYB"
    m, n = len(s1), len(s2)
    print(recursive_longest_common_subsequence(s1, s2, m, n))
    print(recursive_longest_common_subsequence2(s1, s2, 0, 0))
