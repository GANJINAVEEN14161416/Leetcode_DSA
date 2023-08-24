class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        prev=[0]*(amount+1)
        for i in range(amount+1):
            if i%coins[0]==0:
                prev[i]=i//coins[0]
            else:
                prev[i]=float('inf')
        for ind in range(1,n+1):
            cur=[0]*(amount+1)
            for target in range(1,amount+1):
                notpick=prev[target]
                take=float('inf')
                if coins[ind-1]<=target:
                    take=1+cur[target-coins[ind-1]]
                cur[target]=min(take,notpick)
            prev=cur
        if cur[amount]==float('inf'):
            return -1
        return cur[amount]
        
        