#User function Template for python3

class Solution:
    def kosaraju(self, V, adj):
        #Step 1 : Store the vertices based on their finish time
        stack = []
        visited = [False] * V
        
        def dfs(v):
            visited[v] = True
            for u in adj[v] :
                if not visited[u]:
                    dfs(u)
            stack.append(v)
            
        for v in range(V):
            if not visited[v]:
                dfs(v)
        
        '''Step2 : Reverse all edges 
        create a new adj list and store edges in reversed order'''
        
        reversed_edges_list = [[] for i in range(V)]
        
        for v in range(V):
            for u in adj[v]:
                reversed_edges_list[u].append(v)
                
        #Step 3 : DFS on reversed graph in stack
        #count the strongly connected components
        count = 0
        visited = [False]*V
        
        def reverse_DFS(v):
            visited[v] = True
            for u in reversed_edges_list[v]:
                if not visited[u]:
                    reverse_DFS(u)
                    
        while stack:
            v = stack.pop()
            if not visited[v]:
                reverse_DFS(v)
                count+=1
                
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import OrderedDict 
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
        
        print(ob.kosaraju(V, adj))
# } Driver Code Ends