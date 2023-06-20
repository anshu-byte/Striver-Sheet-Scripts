class Solution:
    def findMaxConsecutiveOnes(self, nums):
        res = 0
        n = len(nums)
        if n==1 and nums[0]:
            return 1
        if n==1 and nums[0]!=1:
            return 0
        currCount = 0
        for i in range(n):
            if nums[i]==1:
                currCount += 1
            else:
                currCount = 0
            res = max(currCount,res)
        return res
sol = Solution()
# nums = [1,1,0,1,1,1]
nums = [1,0,1,1,0,1]
print(sol.findMaxConsecutiveOnes(nums))

