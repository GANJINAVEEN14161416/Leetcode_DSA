class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n=len(nums)
        left=0
        right=n-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return True
            if nums[mid]==nums[left]==nums[right]:
                left+=1
                right-=1
            elif nums[left]<=nums[mid]:
                if nums[left]<=target and nums[mid]>=target:
                    right=mid-1
                else:
                    left=mid+1
            else:
                if nums[mid]<=target and nums[right]>=target:
                    left=mid+1
                else:
                    right=mid-1
        return False
        
        