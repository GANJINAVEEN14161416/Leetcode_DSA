class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        q=deque()
        r1,c1=0,0
        if grid[0][0]==1:
            return -1
        q.append([1,r1,c1])
        m1=[[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1]]
        rowl=len(grid)
        coll=len(grid[0])
        visit=[[False]*coll for i in range(rowl)]
        visit[r1][c1]=True
        r2=len(grid)-1
        c2=len(grid)-1
        while q:
            dis,r,c=q.popleft()
            if r==r2 and c==c2 and visit[r][c]:
                return dis
                break
            for new in range(8):
                row=m1[new][0]+r
                col=m1[new][1]+c
                if row>=0 and row<rowl and col>=0 and col<coll and grid[row][col]==0 and not visit[row][col]:
                        print(row,col)
                        visit[row][col]=True
                        q.append([dis+1,row,col])
        if visit[r2][c2]==False:
            return -1
        else:
            return dis
        
        
        