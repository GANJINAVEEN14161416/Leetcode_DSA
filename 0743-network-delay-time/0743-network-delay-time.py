class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distance=[float('inf')]*(n+1)
        q=deque()
        distance[0]=-1
        adj=defaultdict(list)
        for u,v,w in times:
            adj[u].append([v,w])
        q.append([0,k])
        distance[k]=0
        while q:
            dis,node=q.popleft()
            for child,wei in adj[node]:
                if dis+wei<distance[child]:
                    distance[child]=dis+wei
                    q.append([dis+wei,child])
        for i in distance[1:]:
            if i==float('inf'):
                return -1
        return max(distance[1:])
        
        