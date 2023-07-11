class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(visit,i,j,grid,m1,m2):
            visit[i][j]=True
            for change in range(4):
                i1=i+m1[change]
                j1=j+m2[change]
                if i1>=0 and i1<len(grid) and j1>=0 and j1<len(grid[0]) and not visit[i1][j1] and grid[i1][j1]=="1":
                    dfs(visit,i1,j1,grid,m1,m2)
        m1=[0,1,0,-1]
        m2=[1,0,-1,0]
        count=0
        row=len(grid)
        col=len(grid[0])
        visit=[[False]*col for i in range(row)]
        for i in range(row):
            for j in range(col):
                if not visit[i][j] and grid[i][j]=="1":
                    count+=1
                    dfs(visit,i,j,grid,m1,m2)
                    
        return count