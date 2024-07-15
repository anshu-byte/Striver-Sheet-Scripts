from Base.longest_common_subsequence import longest_common_subsequence2


# A supersequence is defined as the string which contains both the strings S1 and S2 as subsequences.
def print_shortest_common_supersequence(s1, s2):
    m, n = len(s1), len(s2)
    lcs = longest_common_subsequence2(s1, s2, m, n)
    return m + n - lcs


if __name__ == "__main__":
    s1 = "geek"
    s2 = "eke"
    l = [
        "",
        "g",
        "e",
        "e",
        "k",
        "s",
        "ge",
        "ge",
        "gk",
        "gs",
        "ee",
        "ek",
        "es",
        "ek",
        "es",
        "ks",
        "gee",
        "gek",
        "ges",
        "gek",
        "ges",
        "gks",
        "eek",
        "ees",
        "eks",
        "eks",
        "geek",
        "gees",
        "geks",
        "geks",
        "eeks",
        "geks",
        "geeks",
    ]
    print(len(l))
    print(shortest_common_supersequence(s1, s2))
