class Solution:
    def maxProfit(self, arr: List[int]) -> int:
        buy=arr[0]
        sell=0
        n=len(arr)
        profit=0
        for i in range(1,n):
            if arr[i]<buy:
                buy=arr[i]
            if arr[i]>buy:
                sell=arr[i]
                profit=max(profit,sell-buy)
        return profit
                
        
                
        
        