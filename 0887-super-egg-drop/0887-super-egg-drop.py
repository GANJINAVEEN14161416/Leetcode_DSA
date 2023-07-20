class Solution:
    def superEggDrop(self, n: int, k: int) -> int:
        dp = [[0]*(n+1) for _ in range(k+1)]
        for i in range(1,k+1):
            for j in range(1,n+1):
                dp[i][j] = 1+dp[i-1][j-1]+dp[i-1][j]
                if dp[i][j]>=k:
                    return i
        