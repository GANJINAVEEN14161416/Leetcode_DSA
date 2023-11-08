class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m=len(matrix)
        n=len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    for col in range(n):
                        if matrix[i][col]!=0:
                            matrix[i][col]="#"
                    for row in range(m):
                        if matrix[row][j]!=0:
                            matrix[row][j]="#"
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=="#":
                    matrix[i][j]=0
        