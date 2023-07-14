
from collections import *

class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        indegree=[0]*V
        for i in range(V):
            for j in adj[i]:
                indegree[j]+=1
        
        q=deque()
        count=0
        for i in range(V):
            if indegree[i]==0:
                q.append(i)
        while q:
            node=q.popleft()
            count+=1
            for child in adj[node]:
                indegree[child]-=1
                if indegree[child]==0:
                    q.append(child)
        if count==V:
            return False
        return True
                


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