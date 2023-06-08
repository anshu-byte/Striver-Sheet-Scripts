from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])

        # check if there is a 0 in the first row
        first_row_has_zero = False
        for j in range(c):
            if matrix[0][j] == 0:
                first_row_has_zero = True
                break

        # check if there is a 0 in the first column
        first_col_has_zero = False
        for i in range(r):
            if matrix[i][0] == 0:
                first_col_has_zero = True
                break

        # use the first row and first column to mark the corresponding rows and columns as 0
        for i in range(1, r):
            for j in range(1, c):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # set the corresponding rows and columns as 0
        for i in range(1, r):
            for j in range(1, c):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # set the first row and first column as 0 if necessary
        if first_row_has_zero:
            for j in range(c):
                matrix[0][j] = 0

        if first_col_has_zero:
            for i in range(r):
                matrix[i][0] = 0
     
# Time Complexity: O(m*n)
# Space Complexity: O(1)