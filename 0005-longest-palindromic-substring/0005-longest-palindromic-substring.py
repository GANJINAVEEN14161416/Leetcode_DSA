class Solution:
    def longestPalindrome(self, s: str) -> str:
        def pal(s,l,r):
            while(l>=0 and r<len(s)) and s[l]==s[r]:
                    l-=1
                    r+=1
            return l+1,r-1
        start,end=0,0
        
        for i in range(len(s)):
            l,r=pal(s,i,i)
            if (r-l)>abs(start-end):
                start=l
                end=r
            l,r=pal(s,i,i+1)
            if (r-l)>(end-start):
                start=l
                end=r
        return s[start:end+1]
        