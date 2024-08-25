from Base.longest_common_subsequence import longest_common_subsequence2


def minimum_no_of_deletion_or_insertion_required_to_convert_string_one_to_another(
    s1, s2
):
    m, n = len(s1), len(s2)
    lcs = longest_common_subsequence2(s1, s2, m, n)
    no_of_deletion = len(s1) - lcs
    no_of_insertion = len(s2) - lcs
    return (no_of_deletion, no_of_insertion)


if __name__ == "__main__":
    s1 = "heap"
    s2 = "pea"
    print(
        "minimum (del,ins):-",
        minimum_no_of_deletion_or_insertion_required_to_convert_string_one_to_another(
            s1, s2
        ),
    )
