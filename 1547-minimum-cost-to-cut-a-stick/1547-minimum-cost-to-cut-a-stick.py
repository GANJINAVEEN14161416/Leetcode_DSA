class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        le=len(cuts)
        cuts=[0]+sorted(cuts)+[n]
        dp=[[-1]*(le+1) for i in range(le+1)]
        def solve(i,j,cuts):
            if i>j:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            mini=float('inf')
            for k in range(i,j+1):
                steps=cuts[j+1]-cuts[i-1]+solve(i,k-1,cuts)+solve(k+1,j,cuts)
                mini=min(mini,steps)
            dp[i][j]=mini
            return mini
        return solve(1,le,cuts)
        
        