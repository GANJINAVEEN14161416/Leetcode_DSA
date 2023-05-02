class Solution:
    def arraySign(self, nums: List[int]) -> int:
        #import math
        answer=0
        for i in nums:
            if i==0:
                return 0
            if i<0:
                answer+=1
        return 1 if answer%2==0 else -1