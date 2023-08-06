class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        n=len(nums)
        flag=False
        if len(nums)==1 and m>=1:
            return True
        if len(nums)==2:
            return True
        for i in range(n-1):
            ans=nums[i]+nums[i+1]
            if ans>=m:
                flag= True
        return flag
  