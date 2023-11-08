class Solution:
    def longestPrefix(self, s: str) -> str:
        ans=""
        n=len(s)
        for i in range(n-1):
            if s[:i+1]==s[-1-i:]:
                if len(s[:i+1])>len(ans):
                    ans=s[:i+1]
        return ans