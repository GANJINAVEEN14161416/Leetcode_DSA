class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        prev=[0]*(amount+1)
        for target in range(amount+1):
            if target%coins[0]==0:
                prev[target]=1
        for ind in range(1,n):
            cur=[0]*(amount+1)
            for target in range(amount+1):
                notpick=prev[target]
                pick=0
                if target>=coins[ind]:
                    pick=cur[target-coins[ind]]
                cur[target]=pick+notpick
            prev=cur
        return prev[amount]
        
        