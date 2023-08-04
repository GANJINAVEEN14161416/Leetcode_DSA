class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        i=0
        if len(s)!=len(goal):
            return False
        n=len(s)
        while i<n:
            if goal==s:
                return True
            store=s[0]
            s=s.replace(s[0],"",1)
            s+=store
            print(s)
            i+=1
        return False
                
        