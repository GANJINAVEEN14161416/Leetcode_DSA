#User function Template for python3


class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        visit=[False]*V
        stack=[False]*V
        def dfs(adj,i,visit,stack):
            visit[i]=True
            stack[i]=True
            for x in adj[i]:
                if stack[x]==True:
                    return True
                if visit[x]==False:
                    if dfs(adj,x,visit,stack):
                        return True
            stack[i]=False
            return False

        for i in range(V):
            if dfs(adj,i,visit,stack):
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