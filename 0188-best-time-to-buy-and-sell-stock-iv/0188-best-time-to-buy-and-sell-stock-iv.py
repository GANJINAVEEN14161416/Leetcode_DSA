class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n=len(prices)
        dp=[[float('-inf')]*(2*k+1) for i in range(n+1)]
        for i in range(n+1):
            dp[i][2*k]=0
        for i in range(2*k+1):
            dp[n][i]=0
        for ind in range(n-1,-1,-1):
            for buy in range(2*k-1,-1,-1):
                if buy%2==0:
                    dp[ind][buy]=max(-prices[ind]+dp[ind+1][buy+1],dp[ind+1][buy])
                else:
                    dp[ind][buy]=max(prices[ind]+dp[ind+1][buy+1],dp[ind+1][buy])
        return dp[0][0]