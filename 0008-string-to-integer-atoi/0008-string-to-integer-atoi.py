class Solution:
    def myAtoi(self, s: str) -> int:
        empty=True
        sign=1
        ans=0
        for i in range(len(s)):
            if empty:
                if s[i]==" ":
                    continue
                elif s[i]=="-":
                    sign=-1
                elif s[i].isdigit():
                    ans=int(s[i])
                elif s[i]!="+":
                    return 0
                empty=False
            
            else:
                if s[i].isdigit():
                    ans=ans*10+int(s[i])
                    if ans*sign>(2**31-1):
                        return 2**31-1
                    elif ans*sign<-2**31:
                        return -2**31
                else:
                    break
        return ans*sign