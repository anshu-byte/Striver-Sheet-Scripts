from typing import List


class Solution:
    # def subsetsWithDup(self, nums):
    #     s = set()
    #     n = len(nums)
    #     def rec(s,res,nums,index,n):
    #         if index>=n:
    #             res.sort()
    #             s.add(tuple(res))
    #             return
    #         rec(s,res+[nums[index]],nums,index+1,n)
    #         rec(s,res,nums,index+1,n)
    #     rec(s,[],nums,0,n)
    #     return [list(i) for i in s]

    def subsetsWithDup(self, nums):
        ans = []
        ds = []
        def findSubsets(ind: int):
            ans.append(ds[:])
            for i in range(ind, len(nums)):
                if i != ind and nums[i] == nums[i - 1]:
                    continue
                ds.append(nums[i])
                findSubsets(i + 1)
                ds.pop()
        nums.sort()
        findSubsets(0)
        return ans

sol = Solution()
nums = [1,2,2]
print(sol.subsetsWithDup(nums))

