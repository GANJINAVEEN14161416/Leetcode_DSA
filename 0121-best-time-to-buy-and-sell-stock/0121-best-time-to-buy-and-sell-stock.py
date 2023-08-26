class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        buy=prices[0]
        for cost in prices[1:]:
            if cost<buy:
                buy=cost
            ans=max(ans,cost-buy)
        return ans
        