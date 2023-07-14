#User function Template for python3
from collections import *
from typing import List

class Solution:    
    def eventualSafeNodes(self, V : int, adj1 : List[List[int]]) -> List[int]:
        adj=defaultdict(list)
        for i in range(V):
            for j in adj1[i]:
                adj[j].append(i)
        indegree=[0]*V
        for i in range(V):
            for j in adj[i]:
                indegree[j]+=1
        q=deque()
        ans=[]
        for i in range(V):
            if indegree[i]==0:
                q.append(i)
        while q:
            node=q.popleft()
            ans.append(node)
            for child in adj[node]:
                indegree[child]-=1
                if indegree[child]==0:
                    q.append(child)
        return sorted(ans)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T = int(input())
    for t in range(T):
        
        V, E = map(int, input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u, v = map(int, input().strip().split())
            adj[u].append(v)
        obj = Solution()
        ans = obj.eventualSafeNodes(V, adj)
        for nodes in ans:
            print(nodes, end = ' ')
        print()
            


# } Driver Code Ends