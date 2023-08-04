class Solution:
    def maxDepth(self, s: str) -> int:
        out=0
        count=0
        for i in s:
            if i=="(":
                count+=1
                #list1.append(count)
            if i==")":
                count-=1
                #list1.append(count)
            out=max(out,count)
        return out