class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        ways=[0]*(n)
        distance=[float('inf')]*(n)
        adj=defaultdict(list)
        for u,v ,w in roads:
            adj[u].append([v,w])
            adj[v].append([u,w])
        q=[]
        distance[0]=0
        heapq.heappush(q,[0,0])
        mod=10**9+7
        ways[0]=1
        while q:
            dis,node=heapq.heappop(q)
            for child,wei in adj[node]:
                if dis+wei<distance[child]:
                    distance[child]=dis+wei
                    ways[child]=ways[node]
                    heapq.heappush(q,[wei+dis,child])
                elif distance[child]==dis+wei:
                    ways[child]+=ways[node]
        return ways[-1]%mod
    
                
        
        
        