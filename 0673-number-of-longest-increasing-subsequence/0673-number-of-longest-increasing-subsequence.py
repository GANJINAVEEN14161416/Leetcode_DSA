class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[1]*n
        ways=[1]*n
        for cur in range(n):
            for prev in range(cur):
                if nums[cur]>nums[prev]:
                    if 1+dp[prev]>dp[cur]:
                        dp[cur]=dp[prev]+1
                        ways[cur]=ways[prev]
                    elif 1+dp[prev]==dp[cur]:
                        ways[cur]+=ways[prev]
                # elif nums[cur]==nums[prev]:
                #     dp[cur]+=1
                #     ways[cur]+=1
        length=max(dp)
        ans=0
        for i in range(n):
            if dp[i]==length:
                ans+=ways[i]
        return ans
        
                     
        