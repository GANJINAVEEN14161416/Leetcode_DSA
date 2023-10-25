from typing import List
from collections import *
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		vis=[False]*V
		def bfs(i,parent):
    		q=deque()
    		q.append([i,parent])
    		vis[i]=True
    		while q:
    		    x,parent=q.popleft()
    		    for i in adj[x]:
    		        if not vis[i]:
        	            q.append([i,x])
        	            vis[i]=True
    		        elif i!=parent:
    		            return True
    	    return False
		for i in range(V):
		    if not vis[i]:
		        if bfs(i,-1):
		            return True
		return False
		        


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
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends