#User function Template for python3


class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code here
        st=[]
        vis=[False]*(V)
        path=[False]*(V)
        def dfs(child):
            vis[child]=True
            path[child]=True
            for i in adj[child]:
                if path[i]==True:
                    return True
                if not vis[i]:
                    if dfs(i):
                        return True
            path[child]=False
            return False
        for i in range(V):
            if not vis[i]:
                if dfs(i):
                    return True
        return False
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
        
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
# } Driver Code Ends