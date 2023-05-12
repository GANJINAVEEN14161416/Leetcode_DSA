class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        list1=[]
        n=len(nums)
        import numpy as np
        if nums.count(0)>1:
            return [0]*n
        elif nums.count(0)==1:
            index_zero=nums.index(0)
            nums.remove(0)
            product=np.prod(np.array(nums))
            for i in range(n):
                if i==index_zero:
                    list1.append(product)
                else:
                    list1.append(0)
        else:
            product=np.prod(np.array(nums))
            for i in range(n):
                list1.append(product//nums[i])
        return list1