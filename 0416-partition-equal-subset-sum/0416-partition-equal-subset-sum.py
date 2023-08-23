class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summ=sum(nums)
        if summ%2!=0:
            return False
        n=len(nums)
        dp=[[-1]*(summ+1)for j in range(n+1)]
        def solve(ind,target):
            if ind==0:
                dp[ind][target]=(nums[ind]==target)
            if target==0:
                dp[ind][target]=True
            if dp[ind][target]!=-1:
                return dp[ind][target]
            take=solve(ind-1,target)
            nottake=False
            if nums[ind]<=target:
                nottake=solve(ind-1,target-nums[ind])
            dp[ind][target]=take or nottake
            return dp[ind][target]
        return solve(n-1,sum(nums)//2)
            