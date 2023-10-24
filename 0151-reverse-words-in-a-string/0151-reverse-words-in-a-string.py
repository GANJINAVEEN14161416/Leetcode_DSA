class Solution:
    def reverseWords(self, s: str) -> str:
        nums=s.split()
        return " ".join(nums[::-1])
        
        