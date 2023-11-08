class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rev=""
        n=len(s)
        for i in range(n):
            if s[:n-i]==s[:n-i][::-1]:
                return s[n-i:][::-1]+s
        return ""
                
