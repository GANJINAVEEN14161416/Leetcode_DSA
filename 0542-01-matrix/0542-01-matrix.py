class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])
        visit=[[False]*(n) for i in range(m)]
        step=0
        q=deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    q.append([i,j,step])
                    visit[i][j]=True
        fourdirections=[[0,1],[1,0],[-1,0],[0,-1]]
        while q:
            x,y,step=q.popleft()
           
            for i,j in fourdirections:
                newrow=x+i
                newcol=y+j
                if newrow>=0 and newrow<m and newcol>=0 and newcol<n and not visit[newrow][newcol]:
                    mat[newrow][newcol]=step+1
                    q.append([newrow,newcol,step+1])
                    visit[newrow][newcol]=True
        return mat
        