class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        V=len(graph)
        adj=defaultdict(list)
        for i in range(V):
            for j in graph[i]:
                adj[j].append(i)
        indegree=[0]*V
        for i in range(V):
            for j in adj[i]:
                indegree[j]+=1
        q=deque()
        print(indegree)
        for i in range(V):
            if indegree[i]==0:
                q.append(i)
        safe = [False] * V
        ans=[]
        while q:
            node=q.popleft()
            ans.append(node)
            for child in adj[node]:
                indegree[child]-=1
                if indegree[child]==0:
                    q.append(child)
        return sorted(ans)
#         safeNodes = []
#         for i in range(V):
#             if safe[i]:
#                 safeNodes.append(i)
#         return safeNodes
        
            
        


        