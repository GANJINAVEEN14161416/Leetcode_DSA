#User function Template for python3
from collections import *
from typing import List

class Solution:    
    def numberOfEnclaves(self, board: List[List[int]]) -> int:
        q=deque()         
        n=len(board)
        m=len(board[0])
        visit=[[False]*m for i in range(n)]
        for i in range(n):
            for j in range(m):
                if (i==0 or j==0 or j==m-1 or i==n-1) and (board[i][j]==1):
                    q.append([i,j])
                    visit[i][j]=True
        m1=[0,-1,0,1]
        m2=[1,0,-1,0]
        while q:
            r,c=q.popleft()
            for new in range(4):
                newrow=r+m1[new]
                newcol=c+m2[new]
                if newrow>=0 and newrow<n and newcol>=0 and newcol<m and board[newrow][newcol]==1 and not visit[newrow][newcol]:
                    visit[newrow][newcol]=True
                    q.append([newrow,newcol])
        count=0
        for i in range(n):
            for j in range(m):
                if not visit[i][j] and board[i][j]==1:
                    count+=1
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int,input().strip().split())
        grid = []
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])

        obj=Solution()
        print(obj.numberOfEnclaves(grid))
# } Driver Code Ends