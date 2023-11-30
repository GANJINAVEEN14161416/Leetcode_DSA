class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n=max(nums)
        left=1
        right=n
        ans=1e9
        def possible(mid):
            temp=0
            for i in nums:
                temp+=math.ceil(i/mid)
            return temp
        while left<=right:
            mid=(left+right)//2
            temp=possible(mid)
            if temp<=threshold:
                ans=min(ans,mid)
                right=mid-1
            else:
                left=mid+1
        return ans
            
            
        