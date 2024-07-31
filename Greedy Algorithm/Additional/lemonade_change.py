#
# @lc app=leetcode id=860 lang=python
#
# [860] Lemonade Change
#


# @lc code=start
class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        no_of_five, no_of_ten = 0, 0

        for bill in bills:
            if bill == 5:
                no_of_five += 1
            elif bill == 10:
                if no_of_five:
                    no_of_five -= 1
                    no_of_ten += 1
                else:
                    return False
            else:
                if no_of_ten and no_of_five:
                    no_of_ten -= 1
                    no_of_five -= 1
                elif no_of_five >= 3:
                    no_of_five -= 3
                else:
                    return False
        return True


# @lc code=end
