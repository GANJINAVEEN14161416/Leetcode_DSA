
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if sum(nums)<target or (sum(nums)-target)%2==1:
            return 0
        summ=(sum(nums)-target)//2
        n=len(nums)
        dp=[[0]*(summ+1) for i in range(n+1)]
        dp[0][0]=1
        for ind in range(1,n+1):
            for tar in range(summ+1):
                nottake=dp[ind-1][tar]
                take=0
                if nums[ind-1]<=tar:
                    take=dp[ind-1][tar-nums[ind-1]]
                dp[ind][tar]=take+nottake
        return dp[n][summ]
        # if target>sum(nums) or (sum(nums)-target)%2==1:
        #     return 0
        # def subset_sum(a, n, sum):
        #     tab = [[0] * (sum + 1) for i in range(n + 1)]
        #     tab[0][0] = 1
        #     for i in range(1, n + 1):
        #         for j in range(sum + 1):
        #             if a[i - 1] <= j:
        #                 tab[i][j] = tab[i - 1][j] + tab[i - 1][j - a[i - 1]]
        #             else:
        #                 tab[i][j] = tab[i - 1][j]
        #     return tab[n][sum]
        # n=len(nums)
        # return subset_sum(nums,n,(sum(nums)-target)//2)
