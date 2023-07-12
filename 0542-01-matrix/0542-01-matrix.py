class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row=len(mat)
        col=len(mat[0])
        q=deque()
        steps=0
        visit=[[False]*col for i in range(row)]
        for i in range(row):
            for j in range(col):
                if mat[i][j]==0:
                    visit[i][j]=True
                    q.append([i,j,steps])
                mat[i][j]=float('inf')
        m1=[0,-1,0,1]
        m2=[1,0,-1,0]
        while q:
            r,c,steps=q.popleft()
            mat[r][c]=steps
            for new in range(4):
                newrow=r+m1[new]
                newcol=c+m2[new]
                if newrow>=0 and newrow<row and newcol>=0 and newcol<col and not visit[newrow][newcol]:
                    visit[newrow][newcol]=True
                    q.append([newrow,newcol,steps+1])
                    
        return mat
            
            
        
                
          
        