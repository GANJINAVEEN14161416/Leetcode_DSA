class Solution:
    def countSquares(self, grid: List[List[int]]) -> int:
        row=len(grid)
        count=0
        col=len(grid[0])
        dp=[[-1]*col for i in range(row)]
        for i in range(row):
            for j in range(col):
                if i==0 or j==0:
                    dp[i][j]=grid[i][j]
        for i in range(1,row):
            for j in range(1,col):
                if grid[i][j]==0:
                    dp[i][j]=0
                else:
                    dp[i][j]=1+min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])

        for i in range(row):
            for j in range(col):
                count+=dp[i][j]
        return count
        