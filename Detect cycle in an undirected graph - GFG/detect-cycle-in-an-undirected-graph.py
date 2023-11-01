from typing import List
from collections import *
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    visit=[False]*V
		def bfs(i,parent):
		    q=deque()
		    q.append([i,parent])
		    visit[i]=True
		    while q:
		        pop,parent=q.popleft()
		        for child in adj[pop]:
		            if not visit[child]:
    		            q.append([child,pop])
    		            visit[child]=True
    		        elif child!=parent:
    		            return True
		    return False
		    
        for i in range(V):
            if not visit[i]:
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