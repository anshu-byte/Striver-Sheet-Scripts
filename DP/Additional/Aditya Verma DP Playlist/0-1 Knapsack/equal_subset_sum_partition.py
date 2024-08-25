from subset_sum import recursiveSubsetSum


def recursiveEqualSubsetSumPartition(nums):
    sumOfAllNum = sum(nums)
    if sumOfAllNum % 2 == 1:
        return False
    else:
        return recursiveSubsetSum(nums, sumOfAllNum // 2, len(nums))


if __name__ == "__main__":
    nums = [1, 5, 11, 5]
    if recursiveEqualSubsetSumPartition(nums):
        print("exists!")
    else:
        print("doesn't exist")

    nums2 = [1, 2, 3, 4, 5]
    if recursiveEqualSubsetSumPartition(nums2):
        print("exists!")
    else:
        print("doesn't exist")

    nums3 = [1, 2, 3, 4, 5, 6, 7]
    if recursiveEqualSubsetSumPartition(nums3):
        print("exists!")
    else:
        print("doesn't exist")
