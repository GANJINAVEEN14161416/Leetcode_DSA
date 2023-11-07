class Solution:
    def coinChange(self, arr: List[int], amount: int) -> int:
        n=len(arr)
        dp=[[-1]*(amount+1) for i in range(n+1)]
        def solve(ind,amount):
            if ind==0:
                if amount%arr[ind]==0:
                    dp[ind][amount]=amount//arr[ind]
                    return amount//arr[ind]
                else:
                    dp[ind][amount]=float('inf')
                    return float('inf')
            if dp[ind][amount]!=-1:
                return dp[ind][amount]
            else:
                nottake=solve(ind-1,amount)
                take=float('inf')
                if arr[ind]<=amount:
                    take=1+solve(ind,amount-arr[ind])
                dp[ind][amount]=min(take,nottake)
                return min(take,nottake)
        ans=solve(n-1,amount)
        if ans==float('inf'):
            return -1
        return ans
        