class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        open=0
        close=0
        start=0
        output=""
        for i in range(len(s)):
            if s[i]=="(":
                open+=1
            if s[i]==")":
                close+=1
            if open==close:
                output+=s[start+1:i]
                open=0
                close=0
                start=i+1
        return output