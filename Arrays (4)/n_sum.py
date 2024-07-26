class Solution:
    def nSum(self, n, nums, target):
        def twoSum(l, r, target, result, results):
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    results.append(result + [nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif s < target:
                    l += 1
                else:
                    r -= 1

        def nSum(l, r, target, N, result, results):
            if (
                r - l + 1 < N or N < 2 or target < nums[l] * N or target > nums[r] * N
            ):  # early termination
                return
            if N == 2:  # two pointers solve sorted 2-sum problem
                twoSum(l, r, target, result, results)
            else:  # recursively reduce N
                for i in range(l, r + 1):
                    if i == l or nums[i - 1] != nums[i]:
                        nSum(
                            i + 1,
                            r,
                            target - nums[i],
                            N - 1,
                            result + [nums[i]],
                            results,
                        )

        nums.sort()
        results = []
        nSum(0, len(nums) - 1, target, n, [], results)
        return results


sol = Solution()
nums = [2, 7, 7, 11, 4, 1, 7, 7, 15]
target = 32
n = 4
print(sol.nSum(n, nums, target))
