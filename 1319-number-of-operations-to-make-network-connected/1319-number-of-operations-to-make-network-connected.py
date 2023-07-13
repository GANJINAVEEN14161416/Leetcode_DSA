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
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        count=0
        extrawires=0
        obj=Unionfind(n)
        for n1,n2 in connections:
            if obj.find(n1)==obj.find(n2):
                extrawires+=1
            else:
                obj.union(n1,n2)
        for i in range(n):
            if obj.find(i)==i:
                count+=1
        if extrawires>=(count-1):
            return count-1
        else:
            return -1
            

        