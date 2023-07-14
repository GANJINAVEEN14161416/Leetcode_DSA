from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    def dfs(visit,node,parent,adj):
	        visit[node]=True
	        for child in adj[node]:
	            if not visit[child]:
	                if dfs(visit,child,node,adj):
	                    return True
	            elif child!=parent:
	                return True
	        return False
	                
	    visit=[False]*V
		for i in range(V):
		    if not visit[i]:
		        if dfs(visit,i,-1,adj):
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