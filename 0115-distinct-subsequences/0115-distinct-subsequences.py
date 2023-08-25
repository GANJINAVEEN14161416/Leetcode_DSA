class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp=[[-1]*(len(t)+1) for i in range(len(s)+1)]
        def solve(ind1,ind2):
            if ind2<0:
                dp[ind1][ind2]=1
                return 1
            if ind1<0:
                dp[ind1][ind2]=0
                return 0
            if dp[ind1][ind2]!=-1:
                return dp[ind1][ind2]
            if s[ind1]==t[ind2]:
                dp[ind1][ind2]=solve(ind1-1,ind2-1)+solve(ind1-1,ind2)
                return solve(ind1-1,ind2-1)+solve(ind1-1,ind2)
            else:
                dp[ind1][ind2]=solve(ind1-1,ind2)
                return solve(ind1-1,ind2)
        return solve(len(s)-1,len(t)-1)
            
        