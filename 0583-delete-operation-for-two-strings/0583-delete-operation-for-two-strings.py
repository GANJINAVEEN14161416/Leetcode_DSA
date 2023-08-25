class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        text1=word1
        text2=word2
        dp=[[0]*(len(text2)+1) for i in range(len(text1)+1)]
        for ind1 in range(1,len(text1)+1):
            for ind2 in range(1,len(text2)+1):
                if text1[ind1-1]==text2[ind2-1]:
                    dp[ind1][ind2]=1+dp[ind1-1][ind2-1]
                else:
                    first=dp[ind1-1][ind2]
                    second=dp[ind1][ind2-1]
                    dp[ind1][ind2]=max(first,second)
        return len(word1)+len(word2)-2*dp[len(text1)][len(text2)]
        
        