class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        dp=[[-1]*n for i in range(n)]
        for i in range(n):
            dp[n-1][i]=triangle[n-1][i]
        for ind1 in range(n-2,-1,-1):
            for ind2 in range(ind1+1):
                down=triangle[ind1][ind2]+dp[ind1+1][ind2]
                diagonal=dp[ind1+1][ind2+1]+triangle[ind1][ind2]
                dp[ind1][ind2]=min(down,diagonal)
        return dp[0][0]
    
            
    