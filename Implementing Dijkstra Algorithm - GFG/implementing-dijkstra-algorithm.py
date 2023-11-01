from collections import *
class Solution:
    def dijkstra(self, V, adj, S):
        #code here
        distance=[float('inf')]*V
        q=deque()
        q.append([S,0])
        distance[S]=0
        while q:
            node,wei=q.popleft()
            for child,weight in adj[node]:
                if wei+weight<distance[child]:
                    distance[child]=wei+weight
                    q.append([child,distance[child]])
        return distance
            
        
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends