class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        ans=0
        for i in s:
            if i=="(":
                stack.append("(")
            else:
                if stack:
                    stack.pop()
                else:
                    ans+=1
        return len(stack)+ans
        