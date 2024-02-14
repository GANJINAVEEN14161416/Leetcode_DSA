class Solution:
    def check(self, nums: List[int]) -> bool:
        n=len(nums)
        sorted_nums=sorted(nums)
        for i in range(n):
            if sorted_nums==nums:
                return True
            else:
                nums[::]=[nums[-1]]+nums[:-1]
        return False
            

        