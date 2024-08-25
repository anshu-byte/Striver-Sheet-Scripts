class Solution:
    def maxLen(self, n, arr):
        # Code here
        currSum = 0
        hashMap = {}
        res = 0
        hashMap[0] = -1
        for i in range(n):
            currSum += arr[i]
            if currSum not in hashMap:
                hashMap[currSum] = i
            else:
                res = max(i - hashMap[currSum], res)
        return res


sol = Solution()
print(sol.maxLen(8, [15, -2, 2, -8, 1, 7, 10, 23]))  # 5
