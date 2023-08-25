class Solution:
    def shortestCommonSupersequence(self, text1: str, text2: str) -> str:
        dp=[[0]*(len(text2)+1) for i in range(len(text1)+1)]
        for ind1 in range(1,len(text1)+1):
            for ind2 in range(1,len(text2)+1):
                if text1[ind1-1]==text2[ind2-1]:
                    dp[ind1][ind2]=1+dp[ind1-1][ind2-1]
                else:
                    first=dp[ind1-1][ind2]
                    second=dp[ind1][ind2-1]
                    dp[ind1][ind2]=max(first,second)
        ind1=len(text1)
        ind2=len(text2)
        ans=""
        while ind1>0  and ind2>0:
            if text1[ind1-1]==text2[ind2-1]:
                ans+=text1[ind1-1]
                ind1-=1
                ind2-=1
            elif dp[ind1][ind2-1]>dp[ind1-1][ind2]:
                ans+=text2[ind2-1]
                ind2-=1
            else:
                ans+=text1[ind1-1]
                ind1-=1
        while ind1>0:
            ans+=text1[ind1-1]
            ind1-=1
        while ind2>0:
            ans+=text2[ind2-1]
            ind2-=1
        return ans[::-1]
        