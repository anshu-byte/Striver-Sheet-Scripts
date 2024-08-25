class Solution:
    def trap(self, heights):
        # brute force
        # res = 0
        # n = len(heights)
        # for i in range(n):
        #     j = i
        #     leftMaxHeight = 0
        #     while j>=0:
        #         leftMaxHeight = max(leftMaxHeight,heights[j])
        #         j -= 1
        #     j = i
        #     rightMaxHeight = 0
        #     while j<n:
        #         rightMaxHeight = max(rightMaxHeight,heights[j])
        #         j += 1
        #     res += min(rightMaxHeight,leftMaxHeight) - heights[i]
        # return res

        # # better
        # res = 0
        # n = len(heights)
        # leftMax = [0]*n
        # leftMax[0] = heights[0]
        # for i in range(1,n):
        #     leftMax[i] = max(leftMax[i-1],heights[i])
        # rightMax = [0]*n
        # rightMax[n-1] = heights[n-1]
        # for i in range(n-2,-1,-1):
        #     rightMax[i] = max(rightMax[i+1],heights[i])
        # for i in range(n):
        #     res += min(leftMax[i],rightMax[i]) - heights[i]
        # return res

        # Best
        res = 0
        n = len(heights)
        l, r = 0, n - 1
        leftMax, rightMax = 0, 0
        while l < r:
            if heights[l] <= heights[r]:
                if heights[l] <= leftMax:
                    res += leftMax - heights[l]
                else:
                    leftMax = heights[l]
                l += 1
            else:
                if heights[r] <= rightMax:
                    res += rightMax - heights[r]
                else:
                    rightMax = heights[r]
                r -= 1
        return res
