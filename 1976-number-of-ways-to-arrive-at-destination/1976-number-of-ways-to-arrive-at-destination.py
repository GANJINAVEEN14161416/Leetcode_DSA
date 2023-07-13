class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj=defaultdict(list)
        for n1,n2,d in roads:
            adj[n1].append([n2,d])
            adj[n2].append([n1,d])
        ways=[0]*n
        distance=[float('inf')]*n
        ways[0]=1
        distance[0]=0
        pq=[]
        heapq.heappush(pq,[0,0])
        while pq:
            dis,node=heapq.heappop(pq)
            for child,wt in adj[node]:
                if dis+wt<distance[child]:
                    distance[child]=dis+wt
                    ways[child]=ways[node]
                    heapq.heappush(pq,[dis+wt,child])
                elif (dis+wt)==distance[child]:
                    ways[child]+=ways[node]%(10**9+7)
        return ways[-1]%(10**9+7)
                    