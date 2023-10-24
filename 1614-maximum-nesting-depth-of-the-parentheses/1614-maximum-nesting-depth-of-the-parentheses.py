class Solution:
    def maxDepth(self, s: str) -> int:
        maxi=-1
        open=0
        for i in s:
            if i=="(":
                open+=1
            if i==")":
                open-=1
            maxi=max(maxi,open)
        return maxi