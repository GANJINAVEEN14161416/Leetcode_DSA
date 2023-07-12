class Solution:
    def numEnclaves(self, board: List[List[int]]) -> int:
        row=len(board)
        col=len(board[0])
        q=deque()
        visit=[[False]*col for i in range(row)]
        for i in range(row):
            for j in range(col):
                if (i==0 or j==0 or j==col-1 or i==row-1) and board[i][j]==1:
                    q.append([i,j])
                    visit[i][j]=True
        m1=[0,-1,0,1]
        m2=[1,0,-1,0]
        while q:
            r,c=q.popleft()
            for new in range(4):
                newrow=r+m1[new]
                newcol=c+m2[new]
                if newrow>=0 and newrow<row and newcol>=0 and newcol<col and not visit[newrow][newcol] and board[newrow][newcol]==1:
                    visit[newrow][newcol]=True
                    q.append([newrow,newcol])
        count=0
        for i in range(row):
            for j in range(col):
                if not visit[i][j] and board[i][j]==1:
                    count+=1
                    visit[i][j]=True
        return count
                
                    
        
        