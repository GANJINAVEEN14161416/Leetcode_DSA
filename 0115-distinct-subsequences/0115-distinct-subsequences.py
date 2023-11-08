class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m,n=len(s),len(t)
        dp=[[0]*(n+1) for i in range(m+1)]
        for i in range(m):
            dp[i][0]=1
        for ind1 in range(1,m+1):
            for ind2 in range(1,n+1):
                if s[ind1-1]==t[ind2-1]:
                    dp[ind1][ind2]=dp[ind1-1][ind2-1]+dp[ind1-1][ind2]
                else:
                    dp[ind1][ind2]=dp[ind1-1][ind2]
        return dp[-1][-1]
        
        
        