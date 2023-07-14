#User function Template for python3
from collections import *
from typing import List
from queue import Queue
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        q=deque()
        q.append(0)
        ans=[]
        visit=[False]*V
        visit[0]=True
        ans.append(0)
        while q:
            pop=q.popleft()
            for child in adj[pop]:
                if not visit[child]:
                    q.append(child)
                    ans.append(child)
                    visit[child]=True
        return ans


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