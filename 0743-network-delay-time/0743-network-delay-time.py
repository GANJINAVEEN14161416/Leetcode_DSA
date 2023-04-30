class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v, w in times:
            graph[u-1].append((v-1, w))

        # Initialize priority queue and distances
        pq = [(0, k-1)]
        dist = [float('inf')] * n
        dist[k-1] = 0

        # Run Dijkstra's algorithm
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))

        # Check if it's possible to send a signal to all nodes
        max_delay = max(dist)
        return max_delay if max_delay != float('inf') else -1





        