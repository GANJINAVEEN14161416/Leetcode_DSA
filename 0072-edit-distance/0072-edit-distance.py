class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp=[[-1]*(len(word2)+1) for i in range(len(word1)+1)]
        def solve(ind1,ind2):
            if ind1==0:
                return ind2
            if ind2==0:
                return ind1
            if dp[ind1][ind2]!=-1:
                return dp[ind1][ind2]
            if word1[ind1-1]==word2[ind2-1]:
                dp[ind1][ind2]=solve(ind1-1,ind2-1)
                return solve(ind1-1,ind2-1)
            insert=solve(ind1-1,ind2)
            delete=solve(ind1,ind2-1)
            replace=solve(ind1-1,ind2-1)
            dp[ind1][ind2]=1+min(insert,delete,replace)
            return 1+min(insert,delete,replace)        
        return solve(len(word1),len(word2))