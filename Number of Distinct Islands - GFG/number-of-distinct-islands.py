#User function Template for python3

import sys
from typing import List
sys.setrecursionlimit(10**8)
class Solution:
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        # code here
        m=len(grid)
        n=len(grid[0])
        visit=[[False]*n for i  in range(m)]
        four_direction=[[0,1],[1,0],[-1,0],[0,-1]]
        def dfs(i,j,x,y,list1):
            visit[i][j]=True
            list1.append((x-i,y-j))
            for a,b in four_direction:
                newrow=i+a
                newcol=j+b
                if newrow>=0 and newrow<m and newcol>=0 and newcol<n and not visit[newrow][newcol] and grid[newrow][newcol]==1:
                    visit[newrow][newcol]=True
                    dfs(newrow,newcol,x,y,list1)
        s=set()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and not visit[i][j]:
                    list1=[]
                    dfs(i,j,i,j,list1)
                    s.add(tuple(list1))
        return len(s)
                    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj=Solution()
        print(obj.countDistinctIslands(grid))
# } Driver Code Ends