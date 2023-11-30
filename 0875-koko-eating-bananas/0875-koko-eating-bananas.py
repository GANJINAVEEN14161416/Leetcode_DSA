class Solution:
    def minEatingSpeed(self, piles, H):
        left=1
        right=max(piles)
        ans=max(piles)
        def findDivisior(mid):
            temp=0
            for i in piles:
                temp+=math.ceil(i/mid)
            return temp
        while left<=right:
            mid=(left+right)//2
            temp=findDivisior(mid)
            if temp<=H:
                ans=min(ans,mid)
                right=mid-1
            else:
                left=mid+1
        return ans
                
        
        