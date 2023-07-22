class Solution:
    def maxProfit(self, arr: List[int]) -> int:
        buy=arr[0]
        ans=0
        for i in range(1,len(arr)):
            if arr[i]<buy:
                buy=arr[i]
            if arr[i]>buy:
                ans=max(ans,arr[i]-buy)
        return ans
                
        
                
        
        