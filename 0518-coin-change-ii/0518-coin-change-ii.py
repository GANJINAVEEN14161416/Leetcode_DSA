class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        dp=[[0]*(amount+1) for i in range(n)]
        for target in range(amount+1):
            if target%coins[0]==0:
                dp[0][target]=1
        for ind in range(1,n):
            for target in range(amount+1):
                notpick=dp[ind-1][target]
                pick=0
                if target>=coins[ind]:
                    pick=dp[ind][target-coins[ind]]
                dp[ind][target]=pick+notpick
        return dp[n-1][amount]
        
        