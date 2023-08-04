class Solution:
    def myAtoi(self, s: str) -> int:
        empty=True
        sign=1
        num=0
        for i in s:
            if empty:
                if i==" ": continue
                elif i=="-":sign=-1
                elif i.isdigit():num=int(i)
                elif i!="+": return 0
                empty=False
            else:
                if i.isdigit():
                    num=num*10+int(i)
                    if sign*num>2**31-1:return 2**31-1
                    elif sign*num<-2**31:return -2**31
                else:
                    break
        return sign*num

