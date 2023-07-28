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
    def removeStones(self, stones: List[List[int]]) -> int:
        max_row=0
        max_col=0
        for i in stones:
            max_row=max(max_row,i[0])
            max_col=max(max_col,i[1])
        obj=Unionfind(max_row+max_col+2)
        s={}
        count=0
        for i in stones:
            n1=i[0]
            n2=i[1]+max_row+1
            obj.union(n1,n2)
            s[n1]=1
            s[n2]=1
            
        for i in s:
            if obj.find(i)==i:
                count+=1
        return len(stones)-count
            