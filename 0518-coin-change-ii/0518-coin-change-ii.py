class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        dp=[[0]*(amount+1) for i in range(n+1)]

        for i in range(n+1):
            dp[i][0]=1
        for ind in range(1,n+1):
            for target in range(1,amount+1):
                notpick=dp[ind-1][target]
                pick=0
                if target>=coins[ind-1]:
                    pick=dp[ind][target-coins[ind-1]]
                dp[ind][target]=pick+notpick
        return dp[n][amount]
        
        