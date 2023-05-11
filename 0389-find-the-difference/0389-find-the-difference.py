class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for i in range(len(t)):
            if s.count(t[i])!=t.count(t[i]):
                return t[i]
        
        
            
        