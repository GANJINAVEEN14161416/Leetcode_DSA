class Solution:
    def minPathSum(self, obstacleGrid: List[List[int]]) -> int:
        n=len(obstacleGrid)
        m=len(obstacleGrid[0])
        dp=[[-1]*m for i in range(n)]
        def solve(ind1,ind2):
            if ind1==0 and ind2==0:
                return obstacleGrid[ind1][ind2]
            if ind1<0 or ind2<0:
                return float('inf')
            if dp[ind1][ind2]!=-1:
                return dp[ind1][ind2]
            else:
                up=0
                down=0
                up=obstacleGrid[ind1][ind2]+solve(ind1-1,ind2)
                down=obstacleGrid[ind1][ind2]+solve(ind1,ind2-1)
                dp[ind1][ind2]=min(up,down)
                return dp[ind1][ind2]
        return solve(n-1,m-1)