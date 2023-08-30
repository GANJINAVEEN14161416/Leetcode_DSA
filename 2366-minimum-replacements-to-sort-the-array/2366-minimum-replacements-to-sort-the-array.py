class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n=len(nums)
        ans=0
        for i in range(n-2,-1,-1):
            if nums[i]>nums[i+1]:
                element=(nums[i]+nums[i+1]-1)//nums[i+1]
                ans+=element-1
                nums[i]=nums[i]//element
        return ans
        