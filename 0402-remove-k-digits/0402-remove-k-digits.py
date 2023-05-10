class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = list()
        for n in num:
            while stack and k and stack[-1] > n:
                stack.pop()
                k -= 1
            
            if stack or n is not '0': # prevent leading zeros
                stack.append(n)
                
        if k: # not fully spent
            stack=stack[0:-k]
            
        return ''.join(stack) or '0'