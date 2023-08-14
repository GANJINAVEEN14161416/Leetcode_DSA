class Solution:
    def longestPrefix(self, s: str) -> str:
        n=len(s)
        ans=0
        s1=""
        for i in range(n-1):
            if s[:i+1]==s[-i-1:]:
                if len(s[:i+1])>ans:
                    s1=s[:i+1]
                    ans=len(s1)
        return s1
                
        