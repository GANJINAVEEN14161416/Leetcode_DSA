class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        prev=[False]*(len(p)+1)
        m=len(s)
        n=len(p)
        prev[0]=True
        for ind2 in range(1,len(p)+1):
            flag=True
            for i in range(ind2):
                if p[i]!="*":
                    flag=False
            prev[ind2]=flag
        for ind1 in range(1,len(s)+1):
            cur=[False]*(n+1)
            for ind2 in range(1,n+1):
                if s[ind1-1]==p[ind2-1] or p[ind2-1]=='?':
                    cur[ind2]=prev[ind2-1]
                if p[ind2-1]=="*":
                    first=prev[ind2]
                    second=cur[ind2-1]
                    cur[ind2]=first or second
            prev=cur
        return prev[n]