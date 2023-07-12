class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row=len(board)
        col=len(board[0])
        q=deque()
        visit=[[False]*col for i in range(row)]
        for i in range(row):
            for j in range(col):
                if (i==0 or j==0 or j==col-1 or i==row-1) and board[i][j]=="O":
                    q.append([i,j])
                    visit[i][j]=True
        print(visit)
        m1=[0,-1,0,1]
        m2=[1,0,-1,0]
        while q:
            r,c=q.popleft()
            for new in range(4):
                newrow=r+m1[new]
                newcol=c+m2[new]
                if newrow>=0 and newrow<row and newcol>=0 and newcol<col and not visit[newrow][newcol] and board[newrow][newcol]=="O":
                    visit[newrow][newcol]=True
                    q.append([newrow,newcol])
        print(visit)
        for i in range(row):
            for j in range(col):
                if not visit[i][j] and board[i][j]=="O":
                    board[i][j]='X'
                    visit[i][j]=True
                
                    
        