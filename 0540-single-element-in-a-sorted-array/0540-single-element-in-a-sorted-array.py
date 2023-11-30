class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        left,right=0,n-1
        if n==1:
            return nums[0]
        while left<=right:
            mid=(left+right)//2
            if nums[mid]!=nums[(mid-1)%n] and nums[(mid+1)%n]!=nums[mid]:
                return nums[mid]
            if mid%2==0:
                if nums[mid]==nums[(mid+1)%n]:
                    left=mid+1
                else:
                    right=mid-1
            else:
                if nums[mid]==nums[(mid-1)%n]:
                    left=mid+1
                else:
                    right=mid-1
        return nums[mid]
        