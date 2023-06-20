class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        adj=defaultdict(list)
        for i,j in connections:
            adj[i].append(j)
            adj[j].append(i)
        if n-1>len(connections):
            return -1
        def dfs(visit,i,adj):
            visit[i]=True
            for j in adj[i]:
                if not visit[j]:
                    dfs(visit,j,adj)
        count=0
        visit=[False]*n
        for r in range(n):
            if not visit[r]:
                count+=1
                dfs(visit,r,adj)
        return count-1
        