class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj=defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j]==1 and i!=j:
                    adj[i+1].append(j+1)            
        V=len(isConnected)
        visit=[0]*(V+1)
        def dfs(node,visit,adj):
            visit[node]=1
            for child in adj[node]:
                if not visit[child]:
                    dfs(child,visit,adj)
            
        count=0
        for i in range(1,V+1):
            if not visit[i]:
                count+=1
                dfs(i,visit,adj)   
        return count
        