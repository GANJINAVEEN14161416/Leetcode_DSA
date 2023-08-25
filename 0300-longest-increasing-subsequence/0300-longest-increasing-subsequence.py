class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[1]*(n)
        ans=1
        for ind in range(n):
            for prev in range(ind):
                if nums[ind]>nums[prev]:
                    dp[ind]=max(1+dp[prev],dp[ind])
                ans=max(ans,dp[ind])
        return ans