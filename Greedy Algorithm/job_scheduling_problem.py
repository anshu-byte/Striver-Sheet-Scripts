class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        sorted_jobs = sorted(Jobs,key=lambda x:x[2],reverse=True)
        max_deadline = max(Jobs,key=lambda x:x[1])[1]
        slots = [-1]*(max_deadline)
        profit = 0
        jobs_done = 0
        for job in sorted_jobs:
            for i in range(job[1]-1,-1,-1):
                if slots[i]==-1:
                    profit += job[2]
                    slots[i] = job[0]
                    break
        for slot in slots:
            if slot!=-1:
                jobs_done += 1
        return jobs_done,profit
            
        
sol = Solution()
# n = 4
# Jobs = [[1,4,20],[2,1,10],[3,1,40],[4,1,30]]
N = 5
Jobs = {(1,2,100),(2,1,19),(3,2,27),
        (4,1,25),(5,1,15)}
print(sol.JobScheduling(Jobs,N))
            
