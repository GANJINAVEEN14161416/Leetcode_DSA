class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        eight_direction=[[-1,1],[1,1],[-1,-1],[1,-1],[0,1],[1,0],[-1,0],[0,-1]]
        if grid[0][0]!=0:
            return -1
        q=deque()
        q.append([0,0,1])
        d1=m-1
        d2=n-1
        visit=[[False]*n for i in range(m)]
        visit[0][0]=True
        while q:
            x,y,steps=q.popleft()
            if visit[d1][d2]==True and x==d1 and y==d2:
                return steps
            for r,c in eight_direction:
                newrow=r+x
                newcol=c+y
                if newrow>=0 and newcol>=0 and newrow<m and newcol<n and grid[newrow][newcol]==0 and not visit[newrow][newcol]:
                    q.append([newrow,newcol,steps+1])
                    visit[newrow][newcol]=True
        if visit[d1][d2]==False:
            return -1
        return steps
                    
            