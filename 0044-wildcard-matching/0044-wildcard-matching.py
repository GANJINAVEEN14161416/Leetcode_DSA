class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp=[[False]*(len(p)+1)for i in range(len(s)+1)]
        m=len(s)
        n=len(p)
        dp[0][0]=True
        for ind2 in range(1,len(p)+1):
            flag=True
            for i in range(ind2):
                if p[i]!="*":
                    flag=False
            dp[0][ind2]=flag
                        
        for ind1 in range(1,len(s)+1):
            for ind2 in range(1,n+1):
                if s[ind1-1]==p[ind2-1] or p[ind2-1]=='?':
                    dp[ind1][ind2]=dp[ind1-1][ind2-1]
                if p[ind2-1]=="*":
                    first=dp[ind1-1][ind2]
                    second=dp[ind1][ind2-1]
                    dp[ind1][ind2]=first or second
        return dp[m][n]
#             dp=[[-1]*(len(p)+1)for i in range(len(s)+1)]
        
#             if ind2>0 and ind1==0:
#                 for i in range(ind2):
#                     if p[i]!="*":
#                         return False
#                 return True
#             if ind1>0 and ind2==0:
#                 return False
#             if dp[ind1][ind2]!=-1:
#                 return dp[ind1][ind2]
#             if s[ind1-1]==p[ind2-1] or p[ind2-1]=='?':
#                 dp[ind1][ind2]=solve(ind1-1,ind2-1)
#                 return solve(ind1-1,ind2-1)
#             if p[ind2-1]=="*":
#                 first=solve(ind1-1,ind2)
#                 second=solve(ind1,ind2-1)
#                 dp[ind1][ind2]=first or second
#                 return first or second
#         return solve(len(s),len(p))
        