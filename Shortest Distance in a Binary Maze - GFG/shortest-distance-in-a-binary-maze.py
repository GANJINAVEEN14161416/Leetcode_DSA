#User function Template for python3
from collections import *
from typing import List

class Solution:
    
    def shortestPath(self, grid: List[List[int]], source: List[int], destination: List[int]) -> int:
        m=len(grid)
        n=len(grid[0])
        eight_direction=[[0,1],[1,0],[-1,0],[0,-1]]
        q=deque()
        s1,s2=source[0],source[1]
        d1,d2=destination[0],destination[1]
        q.append([s1,s2,0])
        visit=[[False]*n for i in range(m)]
        visit[s1][s2]=True
        while q:
            x,y,steps=q.popleft()
            if visit[d1][d2]==True and x==d1 and y==d2:
                return steps
            for r,c in eight_direction:
                newrow=r+x
                newcol=c+y
                if newrow>=0 and newcol>=0 and newrow<m and newcol<n and grid[newrow][newcol]==1 and not visit[newrow][newcol]:
                    q.append([newrow,newcol,steps+1])
                    visit[newrow][newcol]=True
        if visit[d1][d2]==False:
            return -1
        return steps
#{ 
 # Driver Code Starts
#Initial Template for Python 3

         
if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        source = [0] * 2
        source[0], source[1] = map(int,input().strip().split())
        destination = [0] * 2
        destination[0], destination[1] = map(int,input().strip().split())
        obj=Solution()
        print(obj.shortestPath(grid, source, destination))
# } Driver Code Ends