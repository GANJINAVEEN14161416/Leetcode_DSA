class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n=len(weights)
        left=max(weights)
        totalSum=sum(weights)
        right=totalSum
        def Divisior(mid):
            sm=0
            anser=0
            flag=False
            for i in weights:
                if sm+i<=mid:
                    sm+=i
                    
                else:
                    anser+=1
                    sm=i
            if sm:
                anser+=1
            #print(anser)
            return anser
        ans=1e9
        while left<=right:
            mid=(left+right)//2
            temp=Divisior(mid)
            if temp<=days:
                ans=min(ans,mid)
                right=mid-1
            else:
                left=mid+1
        return ans