class Solution:
    def check(self, nums: List[int]) -> bool:
        sorted_nums=sorted(nums)
        n=len(nums)
        for i in range(n-1,-1,-1):
            if sorted_nums==nums:
                return True
            else:
                nums=[nums[-1]]+nums[:-1]
        return False
        