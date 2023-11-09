#User function Template for python3

class Solution:
    def findPath(self, m, n):
        if m[0][0]==0:
            return []
        res=[]
        def dfs(grid,vis,path,row,col):
            n=len(grid)
            if row==n-1 and col==n-1:
                res.append("".join(path[:]))
                
            else:
                vis[row][col]=1
                delrow=[-1,0,1,0]
                delcol=[0,1,0,-1]
                for i in range(4):
                    nr=delrow[i]+row
                    nc=delcol[i]+col
                    if nr>=0 and nr<n and nc>=0 and nc<n and grid[nr][nc]==1 and vis[nr][nc]==0:
                        if [nr,nc]==[row-1,col]:
                            path+=["U"]
                        elif [nr,nc]==[row+1,col]:
                            path+=["D"]
                        elif [nr,nc]==[row,col-1]:
                            path+=["L"]
                        elif [nr,nc]==[row,col+1]:
                            path+=["R"]
                        dfs(grid,vis,path,nr,nc)
                        vis[nr][nc]=0
                        path.pop()
        vis=[[0 for i in range(n)]for j in range(n)]
        dfs(m,vis,[],0,0)
        return res
# Rest of the code remains unchanged
