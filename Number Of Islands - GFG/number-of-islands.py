#User function Template for python3
class Unionfind:
    def __init__(self,n):
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

    def find(self,u):
        if self.parent[u]==u:
            return u
        self.parent[u]=self.find(self.parent[u])
        return self.parent[u]

from typing import List
class Solution:
    def numOfIslands(self, rows: int, cols : int, operators : List[List[int]]) -> List[int]:
        obj=Unionfind(rows*cols)     
        m1=[0,-1,0,1]
        m2=[1,0,-1,0]
        ans=[]
        count=0
        visit=[[0]*m for i in range(n)]
        for row,col in operators:
            if visit[row][col]:
                ans.append(count)
                continue
            visit[row][col]=1
            count+=1
            for i in range(4):
                newrow=row+m1[i]
                newcol=col+m2[i]
                if newrow>=0 and newrow<rows and newcol>=0 and newcol<cols:
                    if visit[newrow][newcol]==1:
                        n1=(newrow*m)+newcol
                        n2=(row*m)+col
                        if obj.find(n1)!=obj.find(n2):
                            count-=1
                            obj.union(n1,n2)
            ans.append(count)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3


    
if __name__=="__main__":
    T = int(input())
    for t in range(T):
        
        n = int(input())
        m = int(input())
        k = int(input())
        operators = []
        for i in range(k):
            u, v = map(int, input().strip().split())
            operators.append([u, v])
        obj = Solution()
        ans = obj.numOfIslands(n, m, operators)
        for i in ans:
            print(i, end = ' ')
        print()
            

# } Driver Code Ends