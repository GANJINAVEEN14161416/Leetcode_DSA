class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp=[[-1]*(len(p)+1)for i in range(len(s)+1)]
        def solve(ind1,ind2):
            if ind2==0 and ind1==0:
                return True
            if ind2>0 and ind1==0:
                for i in range(ind2):
                    if p[i]!="*":
                        return False
                return True
            if ind1>0 and ind2==0:
                return False
            if dp[ind1][ind2]!=-1:
                return dp[ind1][ind2]
            if s[ind1-1]==p[ind2-1] or p[ind2-1]=='?':
                dp[ind1][ind2]=solve(ind1-1,ind2-1)
                return solve(ind1-1,ind2-1)
            if p[ind2-1]=="*":
                first=solve(ind1-1,ind2)
                second=solve(ind1,ind2-1)
                dp[ind1][ind2]=first or second
                return first or second
        return solve(len(s),len(p))
        