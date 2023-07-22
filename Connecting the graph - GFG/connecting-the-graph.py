#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Unionfind:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.rank=[0 for i in range(n)]
    def union(self,u,v):
        parent_u=self.find(u)
        parent_v=self.find(v)
        if parent_u==parent_v:
            return True
        if self.rank[parent_u]<self.rank[parent_v]:
            self.parent[parent_u]=parent_v
            self.rank[parent_v]+=self.rank[parent_u]
        else:
            self.parent[parent_v]=parent_u
            self.rank[parent_u]+=self.rank[parent_v]

    def find(self,u):
        if self.parent[u]==u:
            return u
        self.parent[u]=self.find(self.parent[u])
        return self.parent[u]
class Solution:
    def Solve(self, n, adj):
        obj=Unionfind(n)
        extrawires=0
        count=0
        for n1,n2 in adj:
            if obj.find(n1)==obj.find(n2):
                extrawires+=1
            else:
                obj.union(n1,n2)
        for i in range(n):
            if obj.find(i)==i:
                count+=1
        ans=count-1
        if extrawires>=ans:
            return ans
        else:
            return -1

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n, m = list(map(int, input().split()))
        adj = [list(map(int, input().split())) for _ in range(m)]
        ob = Solution()
        res = ob.Solve(n, adj)
        print(res)
# } Driver Code Ends