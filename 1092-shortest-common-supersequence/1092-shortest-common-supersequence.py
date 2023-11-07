class Solution:
    def shortestCommonSupersequence(self, s1: str, s2: str) -> str:
        x=len(s1)
        y=len(s2)
        dp=[[0]*(y+1) for i in range(x+1)]
        for ind1 in range(1,x+1):
            for ind2 in range(1,y+1):
                if s1[ind1-1]==s2[ind2-1]:
                    dp[ind1][ind2]=1+ dp[ind1-1][ind2-1]
                else:
                    dp[ind1][ind2]=max(dp[ind1-1][ind2],dp[ind1][ind2-1])
        ind1,ind2,ans=x,y,""
        while ind1>0 and ind2>0:
            if s1[ind1-1]==s2[ind2-1]:
                ans+=s2[ind2-1]
                ind1-=1
                ind2-=1
            elif dp[ind1-1][ind2]>dp[ind1][ind2-1]:
                ans+=s1[ind1-1]
                ind1-=1
            else:
                ans+=s2[ind2-1]
                ind2-=1
        while ind1>0:
            ans+=s1[ind1-1]
            ind1-=1
        while ind2>0:
            ans+=s2[ind2-1]
            ind2-=1
        return ans[::-1]
        