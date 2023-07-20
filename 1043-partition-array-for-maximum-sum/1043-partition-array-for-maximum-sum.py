class Solution:
    def maxSumAfterPartitioning(self, nums: List[int], k: int) -> int:
        dp=[-1]*(len(nums)+1)
        def solve(i,nums,k):
            n=len(nums)
            if i==n:
                return 0
            if dp[i]!=-1:
                return dp[i]
            length=0
            maxi=float('-inf')
            ans=float('-inf')
            for ind in range(i,min(i+k,n)):
                length+=1
                maxi=max(maxi,nums[ind])
                sum1=length*maxi+solve(ind+1,nums,k)
                ans=max(ans,sum1)
            dp[i]=ans
            return ans
        return solve(0,nums,k)
            
        