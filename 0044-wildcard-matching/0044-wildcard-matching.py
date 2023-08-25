class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp=[[False]*(len(p)+1)for i in range(len(s)+1)]
        m=len(s)
        n=len(p)
        dp[0][0]=True
        for ind2 in range(1,len(p)+1):
            flag=True
            for i in range(ind2):
                if p[i]!="*":
                    flag=False
                    break
            dp[0][ind2]=flag        
        for ind1 in range(1,len(s)+1):
            for ind2 in range(1,n+1):
                if s[ind1-1]==p[ind2-1] or p[ind2-1]=='?':
                    dp[ind1][ind2]=dp[ind1-1][ind2-1]
                if p[ind2-1]=="*":
                    first=dp[ind1-1][ind2]
                    second=dp[ind1][ind2-1]
                    dp[ind1][ind2]=first or second
        return dp[m][n]

        