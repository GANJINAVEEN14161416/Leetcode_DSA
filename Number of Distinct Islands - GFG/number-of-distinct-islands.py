#User function Template for python3

import sys
from typing import List
sys.setrecursionlimit(10**8)
class Solution:
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        def dfs(i,j,i0,j0,list1):
            visit[i][j]=True
            list1.append((i-i0,j-j0))
            for change in range(4):
                i1=i+m1[change]
                j1=j+m2[change]
                if i1>=0 and i1<len(grid) and j1>=0 and j1<len(grid[0]) and not visit[i1][j1] and grid[i1][j1]==1:
                    dfs(i1,j1,i0,j0,list1)
        m1=[0,1,0,-1]
        m2=[1,0,-1,0]
        count=0
        row=len(grid)
        col=len(grid[0])
        s=set()
        visit=[[False]*col for i in range(row)]
        for i in range(row):
            for j in range(col):
                if not visit[i][j] and grid[i][j]==1:
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