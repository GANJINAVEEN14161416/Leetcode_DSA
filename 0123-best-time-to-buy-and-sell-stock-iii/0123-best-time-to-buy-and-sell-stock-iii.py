class Solution:
    def maxProfit(self, A: List[int]) -> int:
        n=len(A)
        dp=[[[-1 for i in range(3)] for j in range(2)] for k in range(n)]
        # for i in range(n+1):
        #     dp[i][0][n]
        def solve(ind,buy,cap):
            if cap==0 or ind==len(A):
                return 0
            if dp[ind][buy][cap]!=-1:
                return dp[ind][buy][cap]
            if buy:
                profit=max(-A[ind]+solve(ind+1,0,cap),solve(ind+1,1,cap))
            else:
                profit=max(A[ind]+solve(ind+1,1,cap-1),solve(ind+1,0,cap))
            dp[ind][buy][cap]=profit
            return profit
        return solve(0,1,2)
            
            