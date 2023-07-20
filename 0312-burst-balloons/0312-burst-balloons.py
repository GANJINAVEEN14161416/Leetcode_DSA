class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n=len(nums)
        nums=[1]+nums+[1]
        dp=[[-1]*(n+1) for i in range(n+1)]
        def solve(nums,i,j):
            if i>j:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            maxi=float('-inf')
            for k in range(i,j+1):
                steps=nums[i-1]*nums[k]*nums[j+1]+solve(nums,i,k-1)+solve(nums,k+1,j)
                if steps>maxi:
                    maxi=steps
            dp[i][j]=maxi
            return maxi
        return solve(nums,1,n)
        
        