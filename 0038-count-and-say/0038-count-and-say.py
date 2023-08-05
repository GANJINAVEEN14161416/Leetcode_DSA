class Solution:
    def countAndSay(self, n: int) -> str:
        first="1"
        for i in range(n-1):
            s=""
            current=first[0]
            count=1
            for c in first[1:]:
                if c==current:
                    count+=1
                else:
                    s+=str(count)+current
                    current=c
                    count=1
            s+=str(count)+current
            first=s
        return first
        