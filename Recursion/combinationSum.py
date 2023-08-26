class Solution:
    def combinationSum(self, candidates, target):
        s = set()
        n = len(candidates)
        def fun(res,candidates,target,index,n):
            if target<0 or index>=n:
                return 
            if target==0:
                res.sort()
                s.add(tuple(res))
                return
            fun(res+[candidates[index]],candidates,target-candidates[index],index,n)
            fun(res,candidates,target,index+1,n)
        fun([],candidates,target,0,n)
        return [list(i) for i in s]


        