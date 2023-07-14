class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        fresh=0
        q=deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    q.append([i,j,0])
                if grid[i][j]==1:
                    fresh+=1
        visit=[[False]*m for i in range(n)]
        m1=[0,-1,0,1]
        m2=[1,0,-1,0]
        time=0
        count=0
        while q:
            for i in range(len(q)):
                r,c,steps=q.popleft()
                time=max(time,steps)
                for new in range(4):
                    newrow=r+m1[new]
                    newcol=c+m2[new]
                    if newrow>=0 and newrow<n and newcol<m and newcol>=0 and not visit[newrow][newcol] and grid[newrow][newcol]==1:
                        visit[newrow][newcol]=True
                        q.append([newrow,newcol,steps+1])
                        count+=1
        return time if count==fresh else -1
                        
            
        