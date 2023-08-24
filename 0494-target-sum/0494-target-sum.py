
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        summ=sum(nums)-target
        if target>sum(nums):
            return 0
        n=len(nums)
        if summ%2==1:
            return 0
        k=summ//2
        dp=[[0]*(k+1) for i in range(n)]
        if nums[0]==0:
            dp[0][0]=2
        else:
            dp[0][0]=1
        if nums[0]!=0 and nums[0]<=k:
            dp[0][nums[0]]=1
        for ind in range(1,n):
            for tar in range(k+1):
                nottake=dp[ind-1][tar]
                take=0
                if tar>=nums[ind]:
                    take=dp[ind-1][tar-nums[ind]]
                dp[ind][tar]=take+nottake
        return dp[n-1][k]
                        
            
            