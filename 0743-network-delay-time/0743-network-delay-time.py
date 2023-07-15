class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj=defaultdict(list)
        for u,v,w in times:
            adj[u].append([v,w])
        q=[]
        heapq.heappush(q,([0,k]))
        
        distance=[float('inf')]*(n+1)
        distance[k]=0
        while q:
            dis,node=heapq.heappop(q)
            for child,wt in adj[node]:
                if wt+dis<distance[child]:
                    distance[child]=wt+dis
                    heapq.heappush(q,[wt+dis,child])
        return max(distance[1:]) if max(distance[1:])!=float('inf') else -1
