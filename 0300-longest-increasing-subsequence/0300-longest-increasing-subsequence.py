class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[[0]*(len(nums)+1) for i in range(n+1)]        
        for ind in range(n-1,-1,-1):
            for prev_ind in range(ind-1,-2,-1):
                nottake=dp[ind+1][prev_ind]
                take=0
                if prev_ind==-1 or nums[ind]>nums[prev_ind]:
                    take=1+dp[ind+1][ind]
                dp[ind][prev_ind]=max(take,nottake)
        return dp[0][-1]