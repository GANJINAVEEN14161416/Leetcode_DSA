class Solution:
    def minInsertions(self, s: str) -> int:
        text1=s
        text2=s[::-1]
        dp=[[0]*(len(text2)+1) for i in range(len(text1)+1)]
        for ind1 in range(1,len(text1)+1):
            for ind2 in range(1,len(text2)+1):
                if text1[ind1-1]==text2[ind2-1]:
                    dp[ind1][ind2]=1+dp[ind1-1][ind2-1]
                else:
                    first=dp[ind1-1][ind2]
                    second=dp[ind1][ind2-1]
                    dp[ind1][ind2]=max(first,second)
        return len(s)-dp[len(text1)][len(text2)]
        