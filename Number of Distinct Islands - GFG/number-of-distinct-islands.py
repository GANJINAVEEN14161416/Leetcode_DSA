#User function Template for python3

import sys
from typing import List
sys.setrecursionlimit(10**8)
class Solution:
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        # code here
        m=len(grid)
        n=len(grid[0])
        s=set()
        four=[[0,1],[1,0],[-1,0],[0,-1]]
        vis=[[False]*n for i in range(m)]
        def dfs(i,j,first,second):
            lst.append((i-first,j-second))
            vis[i][j]=True
            for a,b in four:
                newrow=i+a
                newcol=j+b
                if newrow>=0 and newrow<m and newcol>=0 and newcol<n and not vis[newrow][newcol] and grid[newrow][newcol]==1:
                    vis[newrow][newcol]=True
                    dfs(newrow,newcol,first,second)
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and not vis[i][j]:
                    lst=[]
                    dfs(i,j,i,j)
                    s.add(tuple(lst))
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