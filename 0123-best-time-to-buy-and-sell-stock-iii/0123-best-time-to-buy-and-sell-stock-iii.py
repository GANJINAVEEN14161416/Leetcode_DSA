class Solution:
    def maxProfit(self, A: List[int]) -> int:
        n=len(A)
        dp=[[[0 for i in range(3)] for j in range(2)] for k in range(n+1)]
        for ind in range(n-1,-1,-1):
            for buy in range(2):
                for cap in range(2):
                    if buy:
                        profit=max(-A[ind]+dp[ind+1][0][cap],dp[ind+1][1][cap])
                    else:
                        profit=max(A[ind]+dp[ind+1][1][cap-1],dp[ind+1][0][cap])
                    dp[ind][buy][cap]=profit
        return dp[0][1][1]
            
            