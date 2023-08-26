class Solution:
    def check(self, A, B, threshold):
        no_of_allocated_students = 1
        pages = 0
        for i in range(len(A)):
            if A[i]>threshold:
                return False
            if pages>threshold:
                no_of_allocated_students += 1
                pages = A[i]
                if no_of_allocated_students>B:
                    return False   
            else:
                pages += A[i]     
        print(no_of_allocated_students)
        return True
    
    def books(self, A, B):
        low = A[0]
        high = sum(A)
        # res = 0
        while(low<=high):
            mid = (low + high)//2
            if self.check(A,B,mid):
                # res = mid
                high = mid - 1
            else:
                low = mid + 1
        return low

sol = Solution()
A = [ 73, 58, 30, 72, 44, 78, 23, 9 ]
B = 5
print(sol.books(A,B))
