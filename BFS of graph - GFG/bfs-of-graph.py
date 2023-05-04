#User function Template for python3

from typing import List
from collections import *
from sys import *
from os import *
from math import *
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # code here
        res = []
        res.append(0)
        q = deque()
        q.append(0)
        while len(q) != 0:
            frst = q.popleft()
            for i in adj[frst]:
                if i not in res:
                    q.append(i)
                    res.append(i)
                    
        return res
                
                
                 


#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends