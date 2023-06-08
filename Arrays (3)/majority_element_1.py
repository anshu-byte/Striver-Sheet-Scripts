# Given an array of N integers, 
# write a program to return an element that occurs more than N/2 times in the given array.
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = float('inf')
        count = 0
        for num in nums:
            if count == 0:
                ans = num
                count += 1
            else:
                if num!=ans:
                    count -= 1
                else:
                    count += 1
        return ans
