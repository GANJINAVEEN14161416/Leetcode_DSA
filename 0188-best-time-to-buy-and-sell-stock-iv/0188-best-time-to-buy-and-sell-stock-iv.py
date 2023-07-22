class Solution:
    def maxProfit(self, k: int, A: List[int]) -> int:
        N=len(A)
        sell=[0]*N
        for _ in range(k):
            buy=-A[0]
            profit=0
            for i in range(1,N):
                buy=max(buy,sell[i]-A[i])
                profit=max(profit,A[i]+buy)
                sell[i]=profit
        return sell[-1]
        