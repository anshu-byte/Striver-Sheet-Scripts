from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 12 5 8765432 -> 12 6 234578 
        # starts looking from backward
        # Find Peak Point, Swap it with Next Greater from digits before peak,
        # Reverse the Bunch of digits(875432)
    
        n = len(nums)
        idx = -1
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                idx = i
                break
                
        if idx == -1:
            nums = nums[::-1]
        else:
            l = n - 1
            k = idx
            while l > k:
                if nums[l] > nums[k]:
                    break
                l -= 1
            nums[k], nums[l] = nums[l], nums[k]
            nums[k+1:] = nums[k+1:][::-1]


# Time Complexity: O(n)
# Space Complexity: O(1)
