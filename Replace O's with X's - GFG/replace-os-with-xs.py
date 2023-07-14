#User function Template for python3
from collections import *
class Solution:
    def fill(self, n, m, board):
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
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        mat = []
        for i in range(n):
            s = list(map(str,input().split()))
            mat.append(s)
        
        ob = Solution()
        ans = ob.fill(n, m, mat)
        for i in range(n):
            for j in range(m):
                print(ans[i][j], end = " ")
            print()
# } Driver Code Ends