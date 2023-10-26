class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj=defaultdict(list)
        for innode,destnode,wt in flights:
            adj[innode].append([destnode,wt])
        q=deque()
        distance=[float('inf')]*n
#         q=deque()
#         heapq.heappush(pq,[0,src,0])
#         distance[src]=0
#         while pq:
#             steps,dis,node=heapq.heappop(pq)
#             if dst==node:
#                 distance[dst]
#             for child,wt in adj[node]:
#                 if dis+wt<distance[child] and steps<=k:
#                     distance[child]=dis+wt
#                     heapq.heappush(pq,[steps+1,dis+wt,child])
#         print(distance)
#         return distance[dst] if distance[dst]!=float('inf') else -1
        q=deque()
        q.append([0,src,0])
        while q:
            dis,node,steps=q.popleft()
            for child,wt in adj[node]:
                if dis+wt<distance[child] and steps<=k:
                    distance[child]=dis+wt
                    q.append([dis+wt,child,steps+1])
        return distance[dst] if distance[dst]!=float('inf') else -1