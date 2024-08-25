from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        start = 0
        end = rows * cols - 1
        while start <= end:
            mid = start + (end - start) // 2
            r_ = mid // cols
            c_ = mid % cols
            if matrix[r_][c_] == target:
                return True
            elif matrix[r_][c_] < target:
                start = mid + 1
            else:
                end = mid - 1
        return False


sol = Solution()
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
# matrix = [[1],[3]]
# matrix = [[1]]
target = 34
print(sol.searchMatrix(matrix, target))
