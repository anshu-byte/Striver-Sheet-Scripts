from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in hashSet:
                curr = num
                currLongest = 1
                while curr + 1 in hashSet:
                    curr += 1
                    currLongest += 1
                longest = max(longest, currLongest)
        return longest

sol = Solution()
print(sol.longestConsecutive([100,4,200,1,3,2])) # 4
        
