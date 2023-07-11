from collections import *
class Solution:

    #Function to find minimum time required to rot all oranges. 
	def orangesRotting(self, grid):
		row=len(grid)
        col=len(grid[0])
        q=deque()
        fresh=0
        visit=[[False]*col for i in range(row)]
        for i in range(row):
            for j in range(col):
                if not visit[i][j] and grid[i][j]==2:
                    q.append([i,j,0])
                    visit[i][j]=True
                if grid[i][j]==1:
                    fresh+=1
                
        m1=[0,-1,0,1]
        m2=[1,0,-1,0]
        time=0
        while q:
            for k in range(len(q)):
                r,c,t=q.popleft()
                time=max(time,t)
                for change in range(4):
                    newrow=r+m1[change]
                    newcol=c+m2[change]
                    if newrow>=0 and newrow<row and newcol>=0 and newcol<col and grid[newrow][newcol]==1 and not visit[newrow][newcol]:
                        q.append([newrow,newcol,t+1])
                        visit[newrow][newcol]=True
                        grid[newrow][newcol]=2
                        fresh-=1
        return time if fresh==0 else -1


#{ 
 # Driver Code Starts
from queue import Queue


T=int(input())
for i in range(T):
	n, m = map(int, input().split())
	grid = []
	for _ in range(n):
		a = list(map(int, input().split()))
		grid.append(a)
	obj = Solution()
	ans = obj.orangesRotting(grid)
	print(ans)

# } Driver Code Ends