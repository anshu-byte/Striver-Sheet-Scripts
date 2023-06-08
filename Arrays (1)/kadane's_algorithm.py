from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        currSum = 0
        for num in nums:
            if currSum < 0:
                currSum = 0
            currSum += num
            if currSum>res:
                res = currSum
        if res<max(nums):
            return max(nums)
        return res
        # 5 4 -1 7 8

# Time Complexity: O(n)
# Space Complexity: O(1)