class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        count=1
        ans=0
        left=0
        n=len(nums)
        for right in range(n):
            count*=nums[right]
            while count>=k:
                count=count//nums[left]
                left+=1
            ans+=right-left+1
        return ans
        