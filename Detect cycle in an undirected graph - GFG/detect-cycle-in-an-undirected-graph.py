from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		parent=[0]*V
		for i in range(V):
		    if not parent[i]:
		        q=[]
		        q.append(i)
		        parent[i]=1
		        while q:
		            poping=q.pop(0)
		            for x in adj[poping]:
		                if not parent[x]:
		                    q.append(x)
		                    parent[x]=poping
		                elif x!=parent[poping]:
		                    return 1
		return 0
		


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