class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans=float('inf')
        left=0
        count=0
        n=len(nums)
        right=1
        count=0
        for i in range(n):
            count+=nums[i]
            while count>=target:
                ans=min(ans,i-left)
                count-=nums[left]
                left+=1
        return ans+1 if ans!=float('inf') else 0
    
        