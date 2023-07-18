class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        x,y=len(s1),len(s2)
        t=[[0]*(y+1) for _ in range(x+1)]
        for i in range(1,x+1):
            for j in range(1,y+1):
                if s1[i-1]==s2[j-1]:
                    t[i][j]=1+t[i-1][j-1]
                else:
                    t[i][j]=max(t[i-1][j],t[i][j-1])
        return t[-1][-1]
        