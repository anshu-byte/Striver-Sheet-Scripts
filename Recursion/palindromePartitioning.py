from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s):
            for i in range(len(s)//2):
                if s[i]!=s[len(s)-1-i]:
                    return False
            return True
        
        res = []
        n = len(s)

        def solve(ind,ds):
            if ind==n:
                res.append(ds)
                return
            for i in range(ind,n):
                ele = s[ind:i+1]
                if(isPalindrome(ele)):
                    solve(i+1,ds+[ele])
            return
        solve(0,[])
        return res
