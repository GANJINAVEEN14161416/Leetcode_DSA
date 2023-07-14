#User function Template for python3
from collections import *
class Solution:
    def numProvinces(self, adj, V):
        graph=defaultdict(list)
        for i in range(len(adj)):
            for j in range(len(adj)):
                if adj[i][j]==1 and i!=j:
                    graph[i+1].append(j+1)
        def dfs(visit,graph,i):
            visit[i]=True
            for child in graph[i]:
                if not visit[child]:
                    dfs(visit,graph,child)
        count=0   
        visit=[False]*(V+1)
        for i in range(1,V+1):
            if not visit[i]:
                count+=1
                dfs(visit,graph,i)
        return count 
                    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        V=int(input())
        adj=[]
        
        for i in range(V):
            temp = list(map(int,input().split()))
            adj.append(temp);
        
        ob = Solution()
        print(ob.numProvinces(adj,V))
# } Driver Code Ends