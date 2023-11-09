from typing import List

class Solution:             
    def solveSudoku(self, board: List[List[str]]) -> None:
        
        """
        Do not return anything, modify board in-place instead.
        """
        assert(self.solve(board))
        return
    
    
    def solve(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                if(board[i][j]=='.'):
                    for k in range(1,10):
                        if(self.isValid(board,i,j,str(k))):
                            board[i][j] = str(k)
                            if(self.solve(board) == True):
                                return True
                            else:
                                board[i][j] = '.'
                    return False
        return True
    
    def isValid(self, board: List[List[str]], row: int, col: int, value: str) -> bool:
        for i in range(9):
            if(board[row][i]== value):
                return False
            if(board[i][col] == value):
                return False
            if(board[3*(row//3)+i//3][3*(col//3)+i%3]== value):
                return False
        return True
        
        