#User function Template for python3
from collections import *
class Solution:
    def numProvinces(self, adj, V):
        # code here 
        graph=[[] for i in range(V+1)]
        for i in range(V):
            for j in range(V):
                if i!=j and adj[i][j]==1:
                    graph[i+1].append(j+1)

        count=0
        vis=[False]*(V+1)
        def bfs(i):
            q=deque()
            q.append(i)
            while q:
                pop=q.popleft()
                for j in graph[pop]:
                    if not vis[j]:
                        q.append(j)
                        vis[j]=True
    
        for i in range(1,V+1):
            if not vis[i]:
                count+=1
                vis[i]=True
                bfs(i)
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