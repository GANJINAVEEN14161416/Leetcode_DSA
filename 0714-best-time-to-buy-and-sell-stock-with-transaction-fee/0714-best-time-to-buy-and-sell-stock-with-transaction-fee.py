class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n=len(prices)
        dp=[[-1]*2 for i in range(n+1)]
        def solve(ind,buy):
            if ind==len(prices):
                return 0
            if dp[ind][buy]!=-1:
                return dp[ind][buy]
            if buy:
                profit=max(-prices[ind]+solve(ind+1,0),solve(ind+1,1))
            else:
                profit=max(prices[ind]-fee+solve(ind+1,1),solve(ind+1,0))
            dp[ind][buy]=profit
            return profit
        return solve(0,1)
        