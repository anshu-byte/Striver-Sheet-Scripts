class Solution:
    def rec(self,res,arr,index,sum,N):
        if index>=N:
            return res.append(sum)
        # not picked
        self.rec(res,arr,index+1,sum,N)
        # picked
        self.rec(res,arr,index+1,sum+arr[index],N)
         
    def subsetSums(self, arr, N):
        # code here
        res = []
        self.rec(res,arr,0,0,N)
        return res