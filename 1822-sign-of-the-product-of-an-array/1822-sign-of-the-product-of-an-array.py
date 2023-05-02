class Solution:
    def arraySign(self, nums: List[int]) -> int:
        #import math
        list1=[]
        for i in nums:
            if i<0:
                list1.append(-1)
            elif i>0:
                list1.append(1)
            else:
                list1.append(0)
        list2=math.prod(list1)
        return list2