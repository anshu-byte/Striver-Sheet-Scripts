# Top - Down
def recursiveSubsetSum(nums, sum, n):
    # Base conditions
    if n == 0 and sum == 0:
        return True

    if n < 0:
        return False

    if nums[n - 1] > sum:  # If nth element is greater than sum, it cannot be included
        return recursiveSubsetSum(nums, sum, n - 1)
    else:
        # Either Include or Exclude to get the desired sum
        return recursiveSubsetSum(nums, sum - nums[n - 1], n - 1) or recursiveSubsetSum(
            nums, sum, n - 1
        )


# Top - Down (Memoization)
def subsetSum(nums, sum, n, dp):
    # Base conditions
    if n == 0 and sum == 0:
        return True

    if n < 0:
        return False

    if dp[n][sum] != -1:
        return dp[n][sum]

    if nums[n - 1] > sum:  # If nth element is greater than sum, it cannot be included
        dp[n][sum] = subsetSum(nums, sum, n - 1, dp)
    else:
        # Either Include or Exclude to get the desired sum
        dp[n][sum] = subsetSum(nums, sum - nums[n - 1], n - 1, dp) or subsetSum(
            nums, sum, n - 1, dp
        )

    return dp[n][sum]


# Bottom - Up
def recursiveSubsetSum2(nums, sum, index):
    # Base conditions
    if sum == 0:
        return True

    if index == len(nums):
        return False

    if (
        nums[index] > sum
    ):  # If index th element is greater than sum, it cannot be included
        return recursiveSubsetSum2(nums, sum, index + 1)
    else:
        # Either Include or Exclude to get the desired sum
        return recursiveSubsetSum2(
            nums, sum - nums[index], index + 1
        ) or recursiveSubsetSum2(nums, sum, index + 1)


# Bottom - Up (Tabulation)
def subsetSum2(nums, sum, n):
    # Initialization
    dp = [[False for _ in range(sum + 1)] for _ in range(n + 1)]
    for row in range(n + 1):
        dp[row][0] = True

    # Traversal
    for row in range(1, n + 1):
        for col in range(1, sum + 1):
            if (
                nums[row - 1] > col
            ):  # If row-1 th element is greater than sum, it cannot be included
                dp[row][col] = dp[row - 1][col]
            else:
                # Either Include or Exclude to get the desired sum
                dp[row][col] = dp[row - 1][col - nums[row - 1]] or dp[row - 1][col]
    return dp[n][sum]


if __name__ == "__main__":
    nums = [2, 3, 7, 8, 10]
    sum = 11
    n = len(nums)
    dp = [[-1 for _ in range(sum + 1)] for _ in range(n + 1)]

    print("Recursive Subset Sum (Top - Bottom)")
    if recursiveSubsetSum(nums, sum, n):
        print("subset sum exists")
    else:
        print("subset sum doesn't exist")
    print()
    print("Subset Sum (Top - Bottom)")
    if subsetSum(nums, sum, n, dp):
        print("subset sum exists")
    else:
        print("subset sum doesn't exist")
    print()
    print("Recursive Subset Sum (Bottom - Top)")
    if recursiveSubsetSum2(nums, sum, 0):
        print("subset sum exists")
    else:
        print("subset sum doesn't exist")
    print()
    print("Subset Sum (Bottom - Top)")
    if subsetSum2(nums, sum, n):
        print("subset sum exists")
    else:
        print("subset sum doesn't exist")
