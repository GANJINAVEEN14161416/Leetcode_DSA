class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[-1]*(n+1) for i in range(m+1)]
        def solve(ind1,ind2):
            if ind1==1 and ind2==1:
                return 1
            if ind1==0  or ind2==0:
                return 0
            if dp[ind1][ind2]!=-1:
                return dp[ind1][ind2]
            dp[ind1][ind2]=solve(ind1-1,ind2)+solve(ind1,ind2-1)
            return dp[ind1][ind2]
        return solve(m,n)