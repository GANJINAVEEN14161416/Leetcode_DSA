class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        dp=[[-1]*(amount+1) for i in range(n+1)]
        def solve(ind,target):
            if target==0:
                dp[ind][target]=1
                return 1
            if ind==0:
                if target%coins[0]==0:
                    dp[ind][target]=1
                    return 1
                else:
                    dp[ind][target]=0
                    return 0
            if dp[ind][target]!=-1:
                return dp[ind][target]
            notpick=solve(ind-1,target)
            pick=0
            if target>=coins[ind]:
                pick=solve(ind,target-coins[ind])
            dp[ind][target]=pick+notpick
            return pick+notpick
        return solve(n-1,amount)
        
        
        