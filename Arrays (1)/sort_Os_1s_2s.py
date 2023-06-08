from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l,h = 0,n-1
        m = 0
        while(m<=h):
            if nums[m]==0:
                nums[m],nums[l] = nums[l],nums[m]
                l +=1
                m += 1
            elif nums[m]==1:
                m+= 1
            else:
                nums[m],nums[h] = nums[h],nums[m]
                h -= 1
    
# Time Complexity: O(n)
# Space Complexity: O(1)