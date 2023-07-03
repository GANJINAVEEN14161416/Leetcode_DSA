class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dic=Counter(nums)
        for i,v in dic.items():
            if v>1:
                return i
            
        