class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n=len(prices)
        dp=[[float('-inf')]*(2*k+1) for i in range(n+1)]
        nxt=[0]*(2*k+1)
        for ind in range(n-1,-1,-1):
            cur=[0]*(2*k+1)
            for buy in range(2*k-1,-1,-1):
                if buy%2==0:
                    cur[buy]=max(-prices[ind]+nxt[buy+1],nxt[buy])
                else:
                    cur[buy]=max(prices[ind]+nxt[buy+1],nxt[buy])
            nxt=cur
        return cur[0]