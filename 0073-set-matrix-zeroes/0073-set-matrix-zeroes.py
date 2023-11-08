class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m=len(matrix)
        n=len(matrix[0])
        iszerorow=False
        iszerocol=False
        for i in range(n):# for first row
            if matrix[0][i]==0:
                iszerorow=True
        for i in range(m):# for first column
            if matrix[i][0]==0:
                iszerocol=True
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==0:
                    matrix[0][j]=0# make first row zero
                    matrix[i][0]=0 # make first column zero
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0]==0 or matrix[0][j]==0:# now make zero on respective row and column
                    matrix[i][j]=0
        if iszerorow==True:
            for i in range(n): # make for first row
                matrix[0][i]=0
        if iszerocol==True:
            for i in range(m):# make for first column
                matrix[i][0]=0
                
            
        