def recursiveCountOfSubsetsWithAGivenSum(nums, sum, n):
    if n == 0 and sum == 0:
        return 1

    if n < 0:
        return 0

    if nums[n - 1] > sum:
        return recursiveCountOfSubsetsWithAGivenSum(nums, sum, n - 1)
    else:
        include = countOfSubsetsWithAGivenSum(nums, sum - nums[n - 1], n - 1, dp)
        exclude = countOfSubsetsWithAGivenSum(nums, sum, n - 1, dp)
        return include + exclude


def countOfSubsetsWithAGivenSum(nums, sum, n, dp):
    if n == 0 and sum == 0:
        return 1

    if n < 0:
        return 0

    if dp[n][sum] != 0:
        return dp[n][sum]

    if nums[n - 1] > sum:
        dp[n][sum] += countOfSubsetsWithAGivenSum(nums, sum, n - 1, dp)
    else:
        include = countOfSubsetsWithAGivenSum(nums, sum - nums[n - 1], n - 1, dp)
        exclude = countOfSubsetsWithAGivenSum(nums, sum, n - 1, dp)
        dp[n][sum] += include + exclude

    return dp[n][sum]


def recursiveCountOfSubsetsWithAGivenSum2(nums, sum, index):
    if sum == 0:
        return 1

    if index == len(nums):
        return 0

    if nums[index] > sum:
        return recursiveCountOfSubsetsWithAGivenSum2(nums, sum, index + 1)
    else:
        include = recursiveCountOfSubsetsWithAGivenSum2(
            nums, sum - nums[index], index + 1
        )
        exclude = recursiveCountOfSubsetsWithAGivenSum2(nums, sum, index + 1)
        return include + exclude


def countOfSubsetsWithAGivenSum2(nums, sum, n):
    dp = [[0 for _ in range(sum + 1)] for _ in range(n + 1)]
    for row in range(n + 1):
        dp[row][0] = 1

    for row in range(1, n + 1):
        for col in range(1, sum + 1):
            if nums[row - 1] > col:
                dp[row][col] = dp[row - 1][col]
            else:
                include = dp[row - 1][col - nums[row - 1]]
                exclude = dp[row - 1][col]
                dp[row][col] = include + exclude
    return dp[n][sum]


if __name__ == "__main__":
    nums = [2, 3, 5, 6, 8, 10]
    sum = 10
    n = len(nums)
    dp = [[0 for _ in range(sum + 1)] for _ in range(n + 1)]
    print(recursiveCountOfSubsetsWithAGivenSum(nums, sum, n))
    print(countOfSubsetsWithAGivenSum(nums, sum, n, dp))
    print(recursiveCountOfSubsetsWithAGivenSum2(nums, sum, 0))
    print(countOfSubsetsWithAGivenSum2(nums, sum, n))
