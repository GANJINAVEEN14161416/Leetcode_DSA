class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if len(s)==0:
            return ""
        if s==s[::-1]:
            return s
        for i in range(len(s)-1,-1,-1):
            if s[:i]==s[:i][::-1]:
                add=s[i:][::-1]
                break
        return add+s