class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        ans=first_point=0
        count=defaultdict(int)
        for moving_point in range(len(nums)):
            count[nums[moving_point]]+=1
            ans=max(ans,count[nums[moving_point]])
            if moving_point-first_point+1-ans>k:
                count[nums[first_point]]-=1
                first_point+=1
        return ans
        