class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n=len(prices)
        dp=[[float('-inf')]*(2*k) for i in range(n)]
        def solve(ind,buy):
            if ind>=len(prices) or buy==2*k:
                return 0
            if dp[ind][buy]!=float('-inf'):
                return dp[ind][buy]
            if buy%2==0:
                dp[ind][buy]=max(-prices[ind]+solve(ind+1,buy+1),solve(ind+1,buy))
                return dp[ind][buy]
            else:
                dp[ind][buy]=max(prices[ind]+solve(ind+1,buy+1),solve(ind+1,buy))
                return dp[ind][buy]
        return solve(0,0)