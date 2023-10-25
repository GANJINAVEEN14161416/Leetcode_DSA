#User function Template for python3

class Solution:
    def numProvinces(self, adj, V):
        # code here 
        ad=[[] for i in range(V+1)]
        for i in range(V):
            for j in range(V):
                if i!=j and adj[i][j]==1:
                    ad[i+1].append(j+1)
        vis=[False]*(V+1)
        ans=[]
        count=0
        def dfs(child):
            vis[child]=True
            for w in ad[child]:
                if not vis[w]:
                    dfs(w)
        for i in range(1,V+1):
            if not vis[i]:
                count+=1
                dfs(i)
        return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        V=int(input())
        adj=[]
        
        for i in range(V):
            temp = list(map(int,input().split()))
            adj.append(temp);
        
        ob = Solution()
        print(ob.numProvinces(adj,V))
# } Driver Code Ends