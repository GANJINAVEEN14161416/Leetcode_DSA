class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        matrix=[[float('inf')]*n for i in range(n)]
        for i in range(n):
            matrix[i][i]=0
        for u,v,w in edges:
            matrix[u][v]=w
            matrix[v][u]=w
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    matrix[i][j]=min(matrix[i][j],matrix[i][k]+matrix[k][j])
        nei=n
        index=-1
        for i in range(n):
            count=0
            for j in range(n):
                if matrix[i][j]<=distanceThreshold:
                    count+=1
            if nei>=count:
                nei=count
                index=i
        return index