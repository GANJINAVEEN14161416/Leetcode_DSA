class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        vis=[[False]*n for i in range(len(grid))]
        q=deque()
        maxi=-1
        ones,cnt=0,0
        step=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append([i,j,0])
                elif grid[i][j]==1:
                    ones+=1
        fourdirections=[[1,0],[0,1],[-1,0],[0,-1]]
        while q:
            x,y,step=q.popleft()
            for i,j in fourdirections:
                newrow=x+i
                newcol=y+j
                if newrow>=0 and newrow<m and newcol>=0 and newcol<n and grid[newrow][newcol]==1 and not vis[newrow][newcol]:
                        q.append([newrow,newcol,step+1])
                        cnt+=1
                        vis[newrow][newcol]=True
        return -1 if cnt!=ones else step