class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s=sorted(s)
        t=sorted(t)
        for i in range(len(t)):
            if t[i] not in s[i:]:
                return t[i]
        
        
            
        