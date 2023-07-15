class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        q=[]
        heapq.heappush(q,[0,0,0])
        n=len(heights)
        m=len(heights[0])
        m1=[0,-1,0,1]
        m2=[1,0,-1,0]
        distance=[[float('inf')]*m for i in range(n)]
        distance[0][0]=0
        while q:
            diff,r,c=heapq.heappop(q)
            for new in range(4):
                newrow=m1[new]+r
                newcol=m2[new]+c
                if newrow>=0 and newrow<n and newcol>=0 and newcol<m:
                    efforts=max(abs(heights[newrow][newcol]-heights[r][c]),diff)
                    if efforts<distance[newrow][newcol]:
                        distance[newrow][newcol]=efforts
                        heapq.heappush(q,[efforts,newrow,newcol])
        return distance[-1][-1] if distance!=float('inf') else -1