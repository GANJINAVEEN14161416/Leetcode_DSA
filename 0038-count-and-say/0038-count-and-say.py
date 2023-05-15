class Solution:
    def countAndSay(self, n: int) -> str:
        first="1"
        for i in range(n-1):
            new=""
            count=1
            current=first[0]
            for c in first[1:]:
                if current==c:
                    count+=1
                else:
                    new+=str(count)+current
                    current=c
                    count=1
            new+=str(count)+current
            first=new
        return first
        