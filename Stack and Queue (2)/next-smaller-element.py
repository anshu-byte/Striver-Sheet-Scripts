class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, nums):
        stack = []
        res = [-1] * len(nums)
        for i, num in enumerate(nums):
            while stack and stack[-1] >= num:
                stack.pop()
            res[i] = -1 if not stack else stack[-1]
            stack.append(num)
        return res
