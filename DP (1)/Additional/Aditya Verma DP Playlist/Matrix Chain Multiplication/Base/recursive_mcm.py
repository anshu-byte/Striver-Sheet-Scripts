def recursive_mcm(nums, i, j):

    if i >= j:
        return 0

    res = float("inf")
    for k in range(i, j):
        temp = (
            recursive_mcm(nums, i, k)
            + recursive_mcm(nums, k + 1, j)
            + nums[i - 1] * nums[k] * nums[j]
        )

        res = min(res, temp)
    return res


if __name__ == "__main__":
    nums1 = [40, 20, 30, 10, 30]
    nums2 = [1, 2, 3, 4, 3]
    n1 = len(nums1)
    n2 = len(nums2)
    dp1 = [[float("inf") for _ in range(n1)] for _ in range(n1)]
    dp2 = [[float("inf") for _ in range(n2)] for _ in range(n2)]
    print(recursive_mcm(nums1, 1, n1 - 1))
    print(recursive_mcm(nums2, 1, n2 - 1))
