class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n=len(prices)
        dp=[[0]*(2*k+1) for i in range(n+1)]
        for ind in range(n-1,-1,-1):
            for trans in range(2*k-1,-1,-1):
                if trans%2==0:
                    profit=max(-prices[ind]+dp[ind+1][trans+1],dp[ind+1][trans])
                else:
                    profit=max(prices[ind]+dp[ind+1][trans+1],dp[ind+1][trans])
                dp[ind][trans]=profit
        return dp[0][0]
#         def solve(ind,trans):
#             if ind==len(prices) or trans==2*k:
#                 return 0
#             if dp[ind][trans]!=-1:
#                 return dp[ind][trans]
#             if trans%2==0:
#                 profit=max(-prices[ind]+solve(ind+1,trans+1),solve(ind+1,trans))
#             else:
                
#                            profit=max(prices[ind]+solve(ind+1,trans+1),solve(ind+1,trans))
#             dp[ind][trans]=profit
#             return profit
#         return solve(0,0)
        