class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        count,temp=0,"01"
        while len(temp)<=len(s):
            if temp in s:
                count=len(temp)
            temp="0"+temp+"1"
        return count

        
                
        