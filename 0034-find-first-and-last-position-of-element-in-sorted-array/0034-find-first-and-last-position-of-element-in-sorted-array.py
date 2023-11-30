class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        def binary(x):
            left,right=0,n-1
            while left<=right:
                mid=(left+right)//2
                if nums[mid]<x:
                    left=mid+1
                else:
                    right=mid-1
            return left
        left=binary(target)
        right=binary(target+1)-1
        if left<=right:
            return [left,right]
        return [-1,-1]