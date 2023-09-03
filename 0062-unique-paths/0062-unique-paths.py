class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0]*(n+1) for i in range(m+1)]
        for ind1 in range(1,m+1):
            for ind2 in range(1,n+1):
                if ind1==ind2==1:
                    dp[ind1][ind2]=1
                else:
                    left=up=0
                    if ind2-1>=0:
                        left=dp[ind1][ind2-1]
                    if ind1-1>=0:
                        up=dp[ind1-1][ind2]
                    dp[ind1][ind2]=up+left
        return dp[-1][-1]