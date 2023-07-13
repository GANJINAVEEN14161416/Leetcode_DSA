#User function Template for python3
from collections import *
import heapq
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        number=defaultdict(list)
        for i in range(V):
            for v in adj[i]:
                number[i].append([v[0],v[1]])
                number[v[0]].append([i,v[1]])
        q=[]
        heapq.heappush(q,[0,0])
        visit=[False]*V
        sum1=0
        while q:
            s,node=heapq.heappop(q)
            if visit[node]:
                continue
            visit[node]=True
            sum1+=s
            for child,wt in number[node]:
                if not visit[child]:
                    heapq.heappush(q,[wt,child])
        return sum1
        


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