class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0]*(n+1) for i in range(m+1)]
        dp[1][1]=1
        for i in range(m+1):
            dp[i][0]=0
        for i in range(n+1):
            dp[0][i]=0
        for ind1 in range(m+1):
            for ind2 in range(n+1):
                if ind1==0 or ind2==0:
                    dp[0][0]=0
                if ind1==1 and ind2==1:
                    dp[1][1]=1
                else:
                    left=0
                    down=0
                    if ind1-1>=0:
                        left=dp[ind1-1][ind2]
                    if ind2-1>=0:
                        down=dp[ind1][ind2-1]
                    dp[ind1][ind2]=left+down
        return dp[m][n]
            
        # def solve(ind1,ind2):
        #     if ind1==1 and ind2==1:
        #         return 1
        #     if ind1==0  or ind2==0:
        #         return 0
        #     if dp[ind1][ind2]!=-1:
        #         return dp[ind1][ind2]
        #     dp[ind1][ind2]=solve(ind1-1,ind2)+solve(ind1,ind2-1)
        #     return dp[ind1][ind2]
        # return solve(m,n)