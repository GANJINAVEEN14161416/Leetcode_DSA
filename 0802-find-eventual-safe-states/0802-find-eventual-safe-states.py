class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        adj=defaultdict(list)
        V=len(graph)
        for i in range(len(graph)):
            for j in graph[i]:
                adj[j].append(i)
        indegree=[0]*V
        for i in range(V):
            for j in adj[i]:
                indegree[j]+=1
        q=deque()
        for j in range(len(indegree)):
            if indegree[j]==0:
                q.append(j)
        ans=[]
        while q:
            n=q.popleft()
            ans.append(n)
            for i in adj[n]:
                indegree[i]-=1
                if indegree[i]==0:
                    q.append(i)
        ans.sort()
        return ans
       