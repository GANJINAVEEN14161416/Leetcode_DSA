class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        n=len(pairs)
        dp=[1]*(n)
        for cur in range(n):
            for prev in range(cur):
                if pairs[cur][0]!=pairs[prev][1] and pairs[cur][0]>pairs[prev][1] and 1+dp[prev]>dp[cur]:
                    dp[cur]=1+dp[prev]
        return max(dp)
        