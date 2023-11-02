class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], sr: int, dst: int, k: int) -> int:
        adj=defaultdict(list)
        for u,v, w in flights:
            adj[u].append([v,w])
        q=deque()
        steps=0
        q.append([0,sr,steps])
        distance=[float('inf')]*n
        distance[sr]=0
        while q:
            dis,s,steps=q.popleft()
            for child,wei in adj[s]:
                if wei+dis<distance[child] and steps<=k:
                    distance[child]=wei+dis
                    q.append([wei+dis,child,steps+1])
        return -1 if distance[dst]==float('inf') else distance[dst]
                    
            
            
        