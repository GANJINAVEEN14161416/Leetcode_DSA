class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        prev=[0]*(len(t)+1)
        for i in range(len(s)+1):
            prev[0]=1
        for ind1 in range(1,len(s)+1):
            cur=[0]*(len(t)+1)
            cur[0]=1
            for ind2 in range(1,len(t)+1):
                if s[ind1-1]==t[ind2-1]:
                    cur[ind2]=prev[ind2-1]+prev[ind2]
                else:
                    cur[ind2]=prev[ind2]
            prev=cur
        return prev[len(t)]
            
        