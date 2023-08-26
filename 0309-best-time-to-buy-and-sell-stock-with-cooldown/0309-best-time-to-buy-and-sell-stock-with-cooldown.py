class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        nxt1=[0]*2
        nxt2=[0]*2
        for ind in range(n-1,-1,-1):
            cur=[0]*2
            for buy in range(2):
                if buy:
                    profit=max(-prices[ind]+nxt1[0],nxt1[1])
                else:
                    profit=max(prices[ind]+nxt2[1],nxt1[0])
                cur[buy]=profit
            nxt2=nxt1
            nxt1=cur
        return cur[1]