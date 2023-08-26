class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n=len(prices)
        nxt=[0]*(2*k+1)
        for ind in range(n-1,-1,-1):
            cur=[0]*(2*k+1)
            for trans in range(2*k-1,-1,-1):
                if trans%2==0:
                    profit=max(-prices[ind]+nxt[trans+1],nxt[trans])
                else:
                    profit=max(prices[ind]+nxt[trans+1],nxt[trans])
                cur[trans]=profit
            nxt=cur
        return nxt[0]
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
        