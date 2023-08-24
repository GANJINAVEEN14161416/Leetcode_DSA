class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp=[[0]*(len(text2)+1) for i in range(len(text1)+1)]
        for ind1 in range(len(text1)):
            for ind2 in range(len(text2)):
                if text1[ind1]==text2[ind2]:
                    dp[ind1][ind2]=1+dp[ind1-1][ind2-1]
                else:
                    first=dp[ind1-1][ind2]
                    second=dp[ind1][ind2-1]
                    dp[ind1][ind2]=max(first,second)
        return dp[len(text1)-1][len(text2)-1]