import heapq
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        #code here
        heap=[]
        distance=[float('inf')]*V
        heapq.heappush(heap,[0,S])
        distance[S]=0
        while heap:
            weight,node=heapq.heappop(heap)
            for node2,wt2 in adj[node]:
                if wt2+weight<distance[node2]:
                    distance[node2]=wt2+weight
                    heapq.heappush(heap,[distance[node2],node2])
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