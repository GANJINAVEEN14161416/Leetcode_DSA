#User function Template for python3

from typing import List
from collections import *
class Solution:
    
    def shortestPath(self, grid: List[List[int]], source: List[int], destination: List[int]) -> int:
        q=deque()
        r1,c1=source[0],source[1]
        q.append([0,r1,c1])
        m1=[0,-1,0,1]
        m2=[1,0,-1,0]
        rowl=len(grid)
        coll=len(grid[0])
        visit=[[float('inf')]*coll for i in range(rowl)]
        visit[r1][c1]=True
        r2=destination[0]
        c2=destination[1]
        while q:
            dis,r,c=q.popleft()
            if r==r2 and c==c2:
                return dis
                break
            for new in range(4):
                row=m1[new]+r
                col=m2[new]+c
                if row>=0 and row<rowl and col>=0 and col<coll and grid[row][col]==1:
                    if dis+1<visit[row][col]:
                        visit[row][col]=1+dis
                        q.append([dis+1,row,col])
        if visit[r2][c2]==float('inf'):
            return -1
        else:
            return dis
        
        
        


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