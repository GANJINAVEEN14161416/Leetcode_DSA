class Solution:
    def canCross(self, stones: List[int]) -> bool:
        mark=defaultdict(int)
        n=len(stones)
        for i in range(n):
            mark[stones[i]]=i
        dp=[[-1]*(n+1) for i in range(n+1)]
        
        def solve(ind,prev):
            if ind>=len(stones)-1:
                return True
            if dp[ind][prev]!=-1:
                return dp[ind][prev]
            ans=False
            for jump in range(prev-1,prev+2):
                if jump>0 and mark[stones[ind]+jump]!=0:
                    ans=ans or solve(mark[stones[ind]+jump],jump)
            dp[ind][prev]=ans
            return ans
        return solve(0,0)
            
        