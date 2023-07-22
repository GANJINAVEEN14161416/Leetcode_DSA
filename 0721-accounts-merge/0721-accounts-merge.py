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

    def find(self,u):
        if self.parent[u]==u:
            return u
        self.parent[u]=self.find(self.parent[u])
        return self.parent[u]

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n=len(accounts)
        obj=Unionfind(n)
        dic={}
        for i in range(n):
            for j in range(1,len(accounts[i])):
                mail=accounts[i][j]
                if mail not in dic:
                    dic[mail]=i
                else:
                    obj.union(dic[mail],i)
        adj=defaultdict(list)
        for mail,i in dic.items():
            val=obj.find(i)
            adj[val].append(mail)
        ans=[]
        for key,val in adj.items():
            ans.append([accounts[key][0]]+sorted(val))
        return ans
            
                    