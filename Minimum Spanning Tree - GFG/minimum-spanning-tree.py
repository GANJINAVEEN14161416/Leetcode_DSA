#User function Template for python3
from collections import *
import heapq
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        graph=defaultdict(list)
        visit=[False]*V
        for i in range(V):
            for v,w in adj[i]:
                graph[i].append([v,w])
        q=[]
        heapq.heappush(q,[0,0])
        ans=0
        while q:
            weight,node=heapq.heappop(q)

            if visit[node]:
                continue
            ans+=weight
            visit[node]=True
            for child,wei in graph[node]:
                if not visit[child]:
                    heapq.heappush(q,[wei,child])
                    
        return ans
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        ob = Solution()
        
        print(ob.spanningTree(V,adj))
# } Driver Code Ends