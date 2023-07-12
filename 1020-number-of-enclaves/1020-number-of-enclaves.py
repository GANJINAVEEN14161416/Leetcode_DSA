class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        visit=[[False]*col for i in range(row)]
        m1=[0,-1,0,1]
        m2=[1,0,-1,0]
        count=0
        def dfs(visit,r,c,grid):
            visit[r][c]=True
            for new in range(4):
                newrow=r+m1[new]
                newcol=c+m2[new]
                if newrow>=0 and newcol<col and newcol>=0 and newrow<row and not visit[newrow][newcol] and grid[newrow][newcol]==1:
                    dfs(visit,newrow,newcol,grid)
        for i in range(row):
            for j in range(col):
                if (i==0 or j==0 or j==col-1 or i==row-1) and grid[i][j]==1:
                    visit[i][j]=True
                    dfs(visit,i,j,grid)
        for i in range(row):
            for j in range(col):
                if not visit[i][j] and grid[i][j]==1:
                    count+=1
        return count
        
        