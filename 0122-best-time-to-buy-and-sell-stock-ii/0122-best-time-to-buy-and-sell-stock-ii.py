class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp=[[0]*2 for i in range(len(prices)+1)]
        n=len(prices)
        dp[n][0]=dp[n][1]=0
        for ind in range(n-1,-1,-1):
            for buy in range(2):
                if buy:
                    profit=max(-prices[ind]+dp[ind+1][0],dp[ind+1][1])
                else:
                    profit=max(prices[ind]+dp[ind+1][1],dp[ind+1][0])
                dp[ind][buy]=profit
        return dp[0][1]
            
            
                