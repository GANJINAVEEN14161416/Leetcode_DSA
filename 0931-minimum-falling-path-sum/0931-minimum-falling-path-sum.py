class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        dp=[[0]*n for i in range(n)]
        for i in range(n):
            dp[n-1][i]=matrix[n-1][i]
        for ind1 in range(n-2,-1,-1):
            for ind2 in range(n-1,-1,-1):
                left,right,below=float('inf'),float('inf'),float('inf')
                if ind1+1<n and ind2-1>=0:
                    left=dp[ind1+1][ind2-1]+matrix[ind1][ind2]
                if ind1+1<n:
                    below=dp[ind1+1][ind2]+matrix[ind1][ind2]
                if ind1+1<n and ind2+1<n:
                    right=dp[ind1+1][ind2+1]+matrix[ind1][ind2]
                dp[ind1][ind2]=min(left,right,below)
        return min(dp[0])
        