from count_no_of_subset_with_a_given_diff import count_no_of_subset_with_a_given_diff


def target_sum(nums, nums_sum):
    return count_no_of_subset_with_a_given_diff(nums, nums_sum)


if __name__ == "__main__":
    nums = [1, 1, 2, 3]
    nums_sum = 1
    print(target_sum(nums, nums_sum))
