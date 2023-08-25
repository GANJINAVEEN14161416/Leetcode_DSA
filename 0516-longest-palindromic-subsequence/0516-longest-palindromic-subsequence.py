class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        n=len(s)
        s2=s[::-1]
        m=len(s2)
        dp=[[0]*(m+1) for i in range(n+1)]
        for ind1 in range(n):
            for ind2 in range(m):
                if s[ind1]==s2[ind2]:
                    dp[ind1][ind2]=1+dp[ind1-1][ind2-1]
                else:
                    f=dp[ind1-1][ind2]
                    second=dp[ind1][ind2-1]
                    dp[ind1][ind2]=max(f,second)
        return dp[n-1][m-1]
        