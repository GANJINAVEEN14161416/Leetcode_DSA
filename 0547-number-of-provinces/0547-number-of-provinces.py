class Unionfind:
    def __init__(self,n=10):
        self.parent=[i for i in range(n+1)]
        self.rank=[0 for i in range(n+1)]
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
        obj=Unionfind(len(isConnected))
        adj=defaultdict(list)
        n=len(isConnected)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]==1:
                    obj.union(i,j)
        count=0
        for i in range(n):
            if obj.find(i)==i:
                count+=1
        return count
        
        

        