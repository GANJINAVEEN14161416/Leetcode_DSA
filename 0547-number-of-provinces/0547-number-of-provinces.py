class Unionfind:
    def __init__(self,n=10):
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
        return False

    def find(self,u):
        if self.parent[u]==u:
            return u
        self.parent[u]=self.find(self.parent[u])
        return self.parent[u]

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        V=len(isConnected)
        obj=Unionfind(V)
        ans=0
        for i in range(V):
            for j in range(V):
                if isConnected[i][j]==1:
                    obj.union(i,j)
        for i in range(V):
            if obj.find(i)==i:
                ans+=1
        return ans
        
        

        