class Solution:
    def longestValidParentheses(self, s: str) -> int:
        open=close=count=0
        for i in s:
            if i=="(":
                open+=1
            if i==")":
                close+=1
            if close==open:
                length=open+close
                print(length)
                count=max(count,length)
            elif close>open:
                open=close=0
        open=close=0
        for i in range(len(s)-1,-1,-1):
            if s[i]=="(":
                open+=1
            if s[i]==")":
                close+=1
            if close==open:
                length=open+close
                count=max(count,length)
            elif open>close:
                open=close=0
        return count
        
        