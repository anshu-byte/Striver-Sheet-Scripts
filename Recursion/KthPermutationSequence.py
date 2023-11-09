class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i for i in range(1, n + 1)]
        factorial = [1] * n
        for i in range(1, n):
            factorial[i] = factorial[i - 1] * i
        k -= 1  
        ans = ''
        fact = 1
        while n > 0:
            index = k // factorial[n - 1]
            ans += str(nums[index])
            nums.pop(index)
            k %= factorial[n - 1]
            n -= 1
        return ans
            
        


        
        