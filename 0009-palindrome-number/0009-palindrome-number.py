class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=str(x)[::-1]
        if x<0:
            return False
        if int(y)==x:
            return True
        else:
            return False
        