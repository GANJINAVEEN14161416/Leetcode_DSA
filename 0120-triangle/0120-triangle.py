class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        dp=[[-1]*n for i in range(n)]
        def solve(ind1,ind2):
            if ind1==n-1:
                dp[ind1][ind2]=triangle[n-1][ind2]
                return triangle[n-1][ind2]
            if dp[ind1][ind2]!=-1:
                return dp[ind1][ind2]
            down=triangle[ind1][ind2]+solve(ind1+1,ind2)
            diagonal=solve(ind1+1,ind2+1)+triangle[ind1][ind2]
            dp[ind1][ind2]=min(down,diagonal)
            return dp[ind1][ind2]
        return solve(0,0)
    
            
    