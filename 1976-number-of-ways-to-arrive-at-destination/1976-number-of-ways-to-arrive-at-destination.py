class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj=defaultdict(list)
        for u,v,w in roads:
            adj[u].append([v,w])
            adj[v].append([u,w])
        distance=[float('inf')]*n
        q=[]
        distance[0]=0
        ways=[0]*n
        ways[0]=1
        heapq.heappush(q,[0,0])
        while q:
            dis,node=heapq.heappop(q)
            for child,wt in adj[node]:
                if wt+dis<distance[child]:
                    distance[child]=wt+dis
                    ways[child]=ways[node]
                    heapq.heappush(q,[wt+dis,child])
                elif wt+dis==distance[child]:
                    ways[child]+=(ways[node])%(10**9+7)
            print(ways)
        return ways[-1]%(10**9+7)
                
        