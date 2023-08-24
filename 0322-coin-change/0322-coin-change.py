class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        dp=[[-1]*(amount+1) for i in range(n+1)]
        def solve(ind,target):
            if ind==0:
                if target%coins[0]==0:
                    dp[ind][target]=target//coins[0]
                    return target//coins[0]
                else:
                    return float('inf')
            if dp[ind][target]!=-1:
                return dp[ind][target]
            else:
                notake=solve(ind-1,target)
                take=float('inf')
                if target>=coins[ind]:
                    take=1+solve(ind,target-coins[ind])
                dp[ind][target]=min(take,notake)
                return min(take,notake)
        ans=solve(n-1,amount)
        if ans==float('inf'):
            return -1
        return ans
        
        
        