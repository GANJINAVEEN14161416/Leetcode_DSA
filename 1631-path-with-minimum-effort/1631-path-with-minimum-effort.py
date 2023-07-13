class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        q=[]
        n=len(heights)
        coll=len(heights[0])
        distance=[[float('inf')]*coll for i in range(n)]
        distance[0][0]=0
        heapq.heappush(q,[0,0,0])
        m1=[0,-1,0,1]
        m2=[1,0,-1,0]
        while q:
            diff,r,c=heapq.heappop(q)
            for i in range(4):
                row=m1[i]+r
                col=m2[i]+c
                if row>=0 and row<n and col>=0 and col<coll:
                    efforts=max(abs(heights[row][col]-heights[r][c]),diff)
                    if efforts<distance[row][col]:
                        distance[row][col]=efforts
                        heapq.heappush(q,[efforts,row,col])
        return distance[-1][-1]