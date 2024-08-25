from count_of_subsets_with_a_given_sum import countOfSubsetsWithAGivenSum2


def count_no_of_subset_with_a_given_diff(nums, diff):
    nums_sum = sum(nums)
    if (nums_sum + diff) % 2 != 0:
        return 0
    target = (nums_sum + diff) // 2
    return countOfSubsetsWithAGivenSum2(nums, target, len(nums))


if __name__ == "__main__":
    nums = [1, 2, 3, 1, 2]
    diff = 1
    nums2 = [1, 1, 2, 3]
    diff2 = 1
    print(count_no_of_subset_with_a_given_diff(nums, diff))
    print(count_no_of_subset_with_a_given_diff(nums2, diff2))
