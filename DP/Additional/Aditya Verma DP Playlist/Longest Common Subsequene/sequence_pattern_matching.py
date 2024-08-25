from Base.longest_common_subsequence import longest_common_subsequence2

if __name__ == "__main__":
    s1 = "axy"
    s2 = "adxcpy"

    if len(s1) == longest_common_subsequence2(s1, s2, len(s1), len(s2)):
        print("Yes, s1 is subsequence of s2")
    else:
        print("no")
