class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1.0
        flag = True
        if n < 0:
            flag = False
            n *= -1.0
        while n > 0:
            if n % 2 == 1:
                ans = ans * x
                n -= 1
            else:
                x = x * x
                n = n // 2
        if flag:
            return ans
        else:
            return 1.0 / ans


if __name__ == "__main__":
    x = 2
    n = 10
    print(Solution().myPow(x, n))
