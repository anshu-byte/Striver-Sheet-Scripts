class Solution:  
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.

    def minimumPlatform(self,n,arr,dep):
        res = 1
        curr = 1
        if n==1:
            return 1
        arr.sort()
        dep.sort()
        
        i,j = 1,0
        while i<n and j<n:
            if arr[i]<=dep[j]:
                curr += 1
                i +=1 
                
            else:
                curr -= 1
                j += 1
                
            res = max(curr,res)
        return res
        


        


        
        
        
