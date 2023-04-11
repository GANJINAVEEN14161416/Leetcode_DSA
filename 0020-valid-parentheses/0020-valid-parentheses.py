class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i in {'(','[','{'}:
                stack.append(i)
            else:
                if stack==[]:
                    return False
                poping=stack.pop()
                if (poping=='(' and i!=')') or (poping=='[' and i!=']') or (poping=='{'!=i!='}'):
                    return False
        return stack==[]

        
        
        # stack=[]
        # for i in s:
        #     if i in {"(","[","{"}:
        #         stack.append(i)
        #     else:
        #         if len(stack)==0:
        #             return False
        #         popped=stack.pop()
        #         if (i==")" and popped!="(") or (i=="]" and popped!="[" )or (popped!="{" and i=="}"):
        #             return False
        # return len(stack)==0