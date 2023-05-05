from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    def dfs(adj,visit,parent,i):
	        visit[i]=True
	        for x in adj[i]:
	            if not visit[x]:
	                if dfs(adj,visit,i,x):
	                    return True
	            elif parent!=x:
	                return True
	        return False
	    
	    
        visit=[False]*V
        for i in range(V):
            if not visit[i]:
                if dfs(adj,visit,2,i):
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