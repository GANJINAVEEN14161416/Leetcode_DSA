import heapq
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        q=[]
        distance=[float('inf')]*V
        distance[S]=0
        heapq.heappush(q,[S,0])
        while q:
            node,dis=heapq.heappop(q)
            for child in adj[node]:
                if child[1]+dis<distance[child[0]]:
                    distance[child[0]]=dis+child[1]
                    heapq.heappush(q,[child[0],distance[child[0]]])
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