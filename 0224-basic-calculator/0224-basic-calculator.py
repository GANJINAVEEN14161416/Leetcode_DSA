class Solution:
    def calculate(self, s: str) -> int:
        def update(sign,value):
            if sign=="+":
                stack.append(value)
            elif sign=="-":
                stack.append(-value)
            elif sign=="*":
                stack.append(stack.pop()*value)
            elif sign=="/":
                stack.append(int(stack.pop()/value))
        i=0
        stack=[]
        num=0
        n=len(s)
        sign="+"
        while i<n:
            #print(stack)
            if s[i].isdigit():
                num=num*10+int(s[i])
            elif s[i] in "+/*-":
                update(sign,num)
                sign=s[i]
                num=0
            elif s[i]=="(":
                num,j=self.calculate(s[i+1:])
                i=j+i
            elif s[i]==")":
                update(sign,num)
                return sum(stack),i+1
            i+=1
        update(sign,num)
        return sum(stack)
        