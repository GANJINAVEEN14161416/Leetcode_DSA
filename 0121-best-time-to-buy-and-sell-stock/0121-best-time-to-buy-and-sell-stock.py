class Solution:
    def maxProfit(self, arr: List[int]) -> int:
        buy=arr[0]
        n=len(arr)
        profit=0
        for i in range(1,n):
            if arr[i]<buy:
                buy=arr[i]
            if arr[i]>buy:
                profit=max(profit,arr[i]-buy)
        return profit
                
        
                
        
        