class Solution:
    def myAtoi(self, s: str) -> int:
        # Skip leading whitespaces
        i = 0
        while i < len(s) and s[i] == " ":
            i += 1

        # Check for optional sign
        if i < len(s) and (s[i] == "+" or s[i] == "-"):
            sign = -1 if s[i] == "-" else 1
            i += 1
        else:
            sign = 1

        # Convert digits to integer
        ans = 0
        max_int, min_int = 2**31 - 1, -(2**31)
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            # Check for overflow
            if ans > (max_int - digit) // 10:
                return max_int if sign == 1 else min_int
            ans = ans * 10 + digit
            print(ans)
            i += 1

        return sign * ans
