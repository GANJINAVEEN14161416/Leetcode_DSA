#User function Template for python3
from collections import *
import heapq
from typing import List
class Solution:
    def minimumCost(self, times: List[List[int]], n : int, k : int) -> int:
        adj=defaultdict(list)
        for u,v,w in times:
            adj[u].append([v,w])
        q=[]
        heapq.heappush(q,([0,k]))
        distance=[float('inf')]*(n+1)
        distance[k]=0
        while q:
            dis,node=heapq.heappop(q)
            for child,wt in adj[node]:
                if wt+dis<distance[child]:
                    distance[child]=wt+dis
                    heapq.heappush(q,[wt+dis,child])
        return max(distance[1:]) if max(distance[1:])!=float('inf') else -1
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

    
if __name__=="__main__":
    T = int(input())
    for t in range(T):
        
        n = int(input())
        k = int(input())
        m = int(input())
        flights = []
        for i in range(m):
            u, v, wt = map(int, input().strip().split())
            flights.append([u, v, wt])
        obj = Solution()
        ans = obj.minimumCost(flights, n, k)
        print(ans)
            

# } Driver Code Ends