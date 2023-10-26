class Solution:
    def minimumEffortPath(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        q=[]
        four_direction=[[1,0],[0,1],[-1,0],[0,-1]]
        heapq.heappush(q,[0,0,0])
        distance=[[float('inf')]*n for i in range(m)]
        distance[0][0]=0
        while q:
            diff,x,y=heapq.heappop(q)
            for r,c in four_direction:
                newrow=x+r
                newcol=y+c
                if newrow>=0 and newcol>=0 and newrow<m and newcol<n:
                    maxi_effort=max(diff,abs(grid[newrow][newcol]-grid[x][y]))
                    if maxi_effort<distance[newrow][newcol]:
                        heapq.heappush(q,[maxi_effort,newrow,newcol])
                        distance[newrow][newcol]=maxi_effort
        return distance[-1][-1]
        