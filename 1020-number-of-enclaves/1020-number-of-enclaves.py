class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        q=deque()
        vis=[[False]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if (i==0 or j==n-1 or j==0 or i==m-1) and grid[i][j]==1:
                    q.append([i,j])
                    vis[i][j]=True
        fourdirect=[[0,1],[1,0],[-1,0],[0,-1]]
        while q:
            x,y=q.popleft()
            for i,j in fourdirect:
                newrow=x+i
                newcol=y+j
                if newrow>=0 and newrow<m and newcol>=0 and newcol<n and grid[newrow][newcol]==1 and not vis[newrow][newcol]:
                    q.append([newrow,newcol])
                    vis[newrow][newcol]=True
        ans=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and not vis[i][j]:
                    ans+=1
        return ans
        