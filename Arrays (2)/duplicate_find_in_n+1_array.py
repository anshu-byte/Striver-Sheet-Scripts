from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tortoise = nums[0]
        hare = nums[0]

        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        tortoise = nums[0]

        while tortoise!=hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        return tortoise
    
# write code to call findDuplicate() function
nums = [1,3,4,2,3]
sol = Solution()
print(sol.findDuplicate(nums))
    
# Time Complexity: O(n)
# Space Complexity: O(1)