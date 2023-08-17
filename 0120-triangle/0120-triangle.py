class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m=len(triangle)
        dp=[[0]*(m) for i in range(m)]
        for ind1 in range(m-1,-1,-1):
            for ind2 in range(ind1,-1,-1):
                if ind1==(m-1):
                    dp[ind1][ind2]=triangle[ind1][ind2]
                else:
                    downleft_diag=triangle[ind1][ind2]+dp[ind1+1][ind2]
                    downright_diag=triangle[ind1][ind2]+dp[ind1+1][ind2+1]
                    dp[ind1][ind2]=min(downleft_diag,downright_diag)
        return dp[0][0]