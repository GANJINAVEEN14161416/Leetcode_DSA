class Solution:
    def reverse(self, x: int) -> int:
        def sign(x):
            if x>=0:
                return 1
            else:
                return -1
        signed=sign(x)
        x=str(abs(x))
        reverse=x[::-1]
        number=signed*int(reverse)
        if abs(number)>=abs(2**31 or 2**31-1):
            return 0
        else:
            return number



        