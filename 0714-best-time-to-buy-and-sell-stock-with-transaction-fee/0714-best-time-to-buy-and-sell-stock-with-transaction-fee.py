class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n=len(prices)
        nxt=[0]*2
        for ind in range(n-1,-1,-1):
            cur=[0]*2
            for buy in range(2):
                if buy:
                    profit=max(-prices[ind]+nxt[0],nxt[1])
                else:
                    profit=max(prices[ind]-fee+nxt[1],nxt[0])
                cur[buy]=profit
            nxt=cur
        return cur[1]
        