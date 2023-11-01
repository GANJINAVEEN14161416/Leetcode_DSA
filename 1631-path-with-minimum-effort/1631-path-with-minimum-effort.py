class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m=len(heights)
        n=len(heights[0])
        distance=[[float('inf')]*n for i in range(m)]
        four_direction=[[1,0],[0,1],[-1,0],[0,-1]]
        q=deque()
        q.append([0,0,0])
        l1,l2=m-1,n-1
        efforts=0
        distance[0][0]=0
        while q:
            r,c,diff=q.popleft()
            for x,y in four_direction:
                newrow=r+x
                newcol=c+y
                if newrow>=0 and newrow<m and newcol>=0 and newcol<n:
                    efforts=max(diff,abs(heights[r][c]-heights[newrow][newcol]))
                    if efforts<distance[newrow][newcol]:
                        distance[newrow][newcol]=efforts
                        q.append([newrow,newcol,efforts])
        return distance[-1][-1]
        