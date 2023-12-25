class Solution:
    def check(self, A, B, threshold):
        no_of_allocated_students = 1
        pages = 0
        for i in range(len(A)):
            if A[i] > threshold:
                return False
            if pages > threshold:
                no_of_allocated_students += 1
                pages = A[i]
                if no_of_allocated_students > B:
                    return False
            else:
                pages += A[i]
        return True

    def books(self, A, B):
        low = max(A)
        high = sum(A)
        while low <= high:
            mid = (low + high) // 2
            if self.check(A, B, mid):
                high = mid - 1
            else:
                low = mid + 1
        return low


sol = Solution()
A = [12, 34, 67, 90]
B = 2
print(sol.books(A, B))
