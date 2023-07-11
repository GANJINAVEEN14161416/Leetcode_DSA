#User function Template for python3

from typing import List
from queue import Queue
from collections import *
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        visit=[0]*V
        q=deque()
        q.append(0)
        ans=[]
        visit[0]=1
        while q:
            for i in range(len(q)):
                x=q.popleft()
                ans.append(x)
                for y in adj[x]:
                    if not visit[y]:
                        q.append(y)
                        visit[y]=1
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