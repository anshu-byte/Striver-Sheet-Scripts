#
# @lc app=leetcode id=55 lang=python
#
# [55] Jump Game
#


# @lc code=start
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        reachable = 0
        for i in range(len(nums)):
            if reachable < i:
                return False
            reachable = max(reachable, i + nums[i])
        return True


# @lc code=end
