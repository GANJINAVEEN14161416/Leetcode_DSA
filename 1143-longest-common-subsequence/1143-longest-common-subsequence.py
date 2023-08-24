class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp=[[-1]*(len(text2)+1) for i in range(len(text1)+1)]
        def solve(ind1,ind2):
            if ind1<0 or ind2<0:
                dp[ind1][ind2]=0
                return 0
            if dp[ind1][ind2]!=-1:
                return dp[ind1][ind2]
            elif text1[ind1]==text2[ind2]:
                dp[ind1][ind2]=1+solve(ind1-1,ind2-1)
                return 1+solve(ind1-1,ind2-1)
            else:
                first=solve(ind1-1,ind2)
                second=solve(ind1,ind2-1)
                dp[ind1][ind2]=max(first,second)
                return max(first,second)
        return solve(len(text1)-1,len(text2)-1)
        