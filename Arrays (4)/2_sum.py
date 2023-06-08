from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = []
        for i in range(len(nums)):
            arr.append([nums[i],i])
        arr = sorted(arr, key =lambda x : x[0])
        l,r = 0,len(nums)-1
        while(l<r):
            sum = arr[l][0] + arr[r][0]
            if sum == target:
                return [arr[l][1],arr[r][1]]
            elif sum < target:
                l += 1
            else:
                r -= 1
sol = Solution()
nums = [2,7,7,11,15]
target = 9
print(sol.twoSum(nums, target))

# Time Complexity: O(nlogn)
# Space Complexity: O(n)