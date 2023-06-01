class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for ind,val in enumerate(nums):
            if val in dic:
                return dic[val],ind
            else:
                dic[target-val]=ind

            
        