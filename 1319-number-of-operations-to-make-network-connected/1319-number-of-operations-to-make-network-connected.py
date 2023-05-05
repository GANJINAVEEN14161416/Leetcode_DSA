class Solution(object):
    def makeConnected(self, n, connections):
        adj=defaultdict(list)
        for x,y in connections:
            adj[x].append(y)
            adj[y].append(x)
        visit=[False]*n
        def dfs(adj,visit,i):
            visit[i]=True
            for x in adj[i]:
                if not visit[x]:
                    dfs(adj,visit,x)
        if len(connections)<(n-1):
            return -1
        count=0
        for i in range(n):
            if not visit[i]:
                dfs(adj,visit,i)
                count+=1
        return count-1
            
        
        