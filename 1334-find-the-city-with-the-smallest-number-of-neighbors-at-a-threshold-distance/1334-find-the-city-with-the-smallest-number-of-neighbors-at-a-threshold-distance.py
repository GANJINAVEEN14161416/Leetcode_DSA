class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        matrix=[[float('inf')]*n for i in range(n)]
        for i,j,w in edges:
            matrix[i][j]=matrix[j][i]=w
        for i  in range(n):
            for j in range(n):
                if i==j:
                    matrix[i][j]=0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    matrix[i][j]=min(matrix[i][j],matrix[i][k]+matrix[k][j])
        index=-1
        ans=float('inf')
        for i in range(n):
            max_city=0
            for j in range(n):
                if matrix[i][j]<=distanceThreshold and matrix[i][j]!=0:
                    max_city+=1
            if max_city<=ans:
                ans=max_city
                index=max(index,i)
        return index
                    
                
        