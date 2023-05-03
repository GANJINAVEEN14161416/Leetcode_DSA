from typing import List
class Solution:
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
            v=[0]*V
            for i in range(V):
                if not v[i]:
                    q = []
                    v[i]=1
                    q.append(i)
                    while q:
                        p= q.pop(0)
                        for x in adj[p]:
                            if not v[x]:
                                q.append(x)
                                v[x] = p
                            elif (x != v[p]):
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