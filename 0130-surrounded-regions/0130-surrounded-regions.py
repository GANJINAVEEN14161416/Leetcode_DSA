class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m=len(board)
        n=len(board[0])
        q=deque()
        vis=[[False]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if (i==0 or j==n-1 or i==m-1 or j==0) and board[i][j]=="O":
                    q.append([i,j])
                    vis[i][j]=True
        fourdirections=[[1,0],[0,1],[-1,0],[0,-1]]
        while q:
            x,y=q.popleft()
            for i,j in fourdirections:
                newrow=x+i
                newcol=y+j
                if newrow>=0 and newrow<m and newcol>=0 and newcol<n and board[newrow][newcol]=="O" and not vis[newrow][newcol]:
                    q.append([newrow,newcol])
                    vis[newrow][newcol]=True
        for i in range(m):
            for j in range(n):
                if not vis[i][j]:
                    board[i][j]="X"
        return board