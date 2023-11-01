#User function Template for python3


class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code here
        visit=[False]*V
        path=[False]*V
        def dfs(i):
            visit[i]=True
            path[i]=True
            for child in adj[i]:
                if path[child]:
                    return True
                elif not visit[child]:
                    if dfs(child):
                        return True
            path[i]=False
        for i in range(V):
            if not visit[i]:
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