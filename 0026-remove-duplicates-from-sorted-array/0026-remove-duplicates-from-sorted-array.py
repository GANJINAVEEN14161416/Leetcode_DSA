class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        set_nums=sorted(list(set(nums)))

        nums[::]=set_nums[::]
        return len(nums)
    
        
        