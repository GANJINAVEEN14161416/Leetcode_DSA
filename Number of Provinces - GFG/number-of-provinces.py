#User function Template for python3
from collections import *
class Solution:
    def numProvinces(self, isConnected, V):
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