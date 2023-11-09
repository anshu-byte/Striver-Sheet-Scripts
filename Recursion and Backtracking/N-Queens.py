class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Empty Board
        board = [['.' for _ in range(n)] for _ in range(n)]
        ans = []

        # Basic Solution
        # def isSafe(row,col,board,n):
        #     r,c = row,col
            
        #     # Left Upward Diagonal Case
        #     while(r>=0 and c>=0):
        #         if board[r][c]=='Q': return False
        #         r -=1
        #         c -=1

        #     r,c = row,col

        #     # Left Coloumn Direction
        #     while(c>=0):
        #         if board[r][c]=='Q': return False
        #         c -=1
            
        #     r,c = row,col

        #     # Left Downward Diagonal Case
        #     while(r<n and c>=0):
        #         if board[r][c]=='Q': return False
        #         r +=1
        #         c -= 1
        #     return True

        # def solve(col,board,ans,n):
        #     if col==n:
        #         ans.append([''.join(row) for row in board])
        #         return
        #     for row in range(n):
        #         if(isSafe(row,col,board,n)):
        #             board[row][col]='Q'
        #             solve(col+1,board,ans,n)
        #             board[row][col]='.'
        # solve(0,board,ans,n)

        # Using Hash for isSafe
        leftRow, upperDiagonal, lowerDiagonal = [0 for i in range(n)],[0 for i in range(2*n-1)],[0 for i in range(2*n-1)]
        def solve1(col):
            if col==n:
                ans.append([''.join(row) for row in board])
                return
            for row in range(n):
                if(leftRow[row]==0 and lowerDiagonal[row+col]==0 and upperDiagonal[n-1+col-row]==0):
                    board[row][col]='Q'
                    leftRow[row]=1
                    lowerDiagonal[row+col]=1
                    upperDiagonal[n-1+col-row]=1
                    solve1(col+1)
                    board[row][col]='.'
                    leftRow[row]=0
                    lowerDiagonal[row+col]=0
                    upperDiagonal[n-1+col-row]=0          
        solve1(0)
        return ans

