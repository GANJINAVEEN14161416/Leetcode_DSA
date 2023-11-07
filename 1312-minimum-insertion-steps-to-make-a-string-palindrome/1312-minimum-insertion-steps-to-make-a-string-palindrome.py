class Solution:
    def minInsertions(self, s: str) -> int:
        x=y=len(s)
        s1=s
        s2=s[::-1]
        dp=[[0]*(y+1) for i in range(x+1)]
        for ind1 in range(1,x+1):
            for ind2 in range(1,y+1):
                if s1[ind1-1]==s2[ind2-1]:
                    dp[ind1][ind2]=1+ dp[ind1-1][ind2-1]
                else:
                    dp[ind1][ind2]=max(dp[ind1-1][ind2],dp[ind1][ind2-1])
        return x-dp[-1][-1]
        