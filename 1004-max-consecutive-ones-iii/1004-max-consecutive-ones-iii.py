class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res=[0]*2
        ans=left=0
        for right in range(len(nums)):
            res[nums[right]]+=1
            ans=max(ans,res[1])
            if (right-left+1)-res[1]>k:
                res[nums[left]]-=1
                left+=1
        return len(nums)-left
            
        