class Solution:
    def sortVowels(self, s: str) -> str:
        n=len(s)
        s=list(s)
        v=[]
        index=[]
        for i in range(len(s)):
            if s[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                v.append(ord(s[i]))
                index.append(i)
        v.sort()
        p=0
        for i,j in zip(index,v):
            s[i]=chr(j)
        return "".join(s)
            
        
        