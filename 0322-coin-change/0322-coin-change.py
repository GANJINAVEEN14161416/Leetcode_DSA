class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        dp=[[0]*(amount+1) for i in range(n+1)]
        for i in range(amount+1):
            if i%coins[0]==0:
                dp[0][i]=i//coins[0]
            else:
                dp[0][i]=float('inf')
        for ind in range(1,n+1):
            for target in range(1,amount+1):
                notpick=dp[ind-1][target]
                take=float('inf')
                if coins[ind-1]<=target:
                    take=1+dp[ind][target-coins[ind-1]]
                dp[ind][target]=min(take,notpick)
        if dp[n][amount]==float('inf'):
            return -1
        return dp[n][amount]
        
        