class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            temp=nums[:i]+nums[i+1:]
            if temp==sorted(set(temp)):
                return True
        return False
        