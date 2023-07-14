class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        q=deque()         
        n=len(board)
        m=len(board[0])
        visit=[[False]*m for i in range(n)]
        for i in range(n):
            for j in range(m):
                if (i==0 or j==0 or j==m-1 or i==n-1) and (board[i][j]=="O"):
                    q.append([i,j])
                    visit[i][j]=True
        m1=[0,-1,0,1]
        m2=[1,0,-1,0]
        while q:
            r,c=q.popleft()
            for new in range(4):
                newrow=r+m1[new]
                newcol=c+m2[new]
                if newrow>=0 and newrow<n and newcol>=0 and newcol<m and board[newrow][newcol]=="O" and not visit[newrow][newcol]:
                    visit[newrow][newcol]=True
                    q.append([newrow,newcol])
        for i in range(n):
            for j in range(m):
                if not visit[i][j] and board[i][j]=="O":
                    board[i][j]="X"
        return board
        
        