#User function Template for python3

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        ans=[]
        visit=[False]*V
        def dfs(adj,visit,i):
            visit[i]=True
            for child in adj[i]:
                if not visit[child]:
                    ans.append(child)
                    dfs(adj,visit,child)
                    
        for i in range(V):
            if not visit[i]:
                ans.append(i)
                dfs(adj,visit,i)
        return ans


#{ 
 # Driver Code Starts

if __name__ == '__main__':
    T=int(input())
    while T>0:
        V,E=map(int,input().split())
        adj=[[] for i in range(V+1)]
        for i in range(E):
            u,v=map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob=Solution()
        ans=ob.dfsOfGraph(V,adj)
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()
        T-=1
# } Driver Code Ends