class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        prev=[0]*(len(text2)+1)
        for ind1 in range(1,len(text1)+1):
            cur=[0]*(len(text2)+1)
            for ind2 in range(1,len(text2)+1):
                if text1[ind1-1]==text2[ind2-1]:
                    cur[ind2]=1+prev[ind2-1]
                else:
                    first=prev[ind2]
                    second=cur[ind2-1]
                    cur[ind2]=max(first,second)
            prev=cur
        return prev[len(text2)]