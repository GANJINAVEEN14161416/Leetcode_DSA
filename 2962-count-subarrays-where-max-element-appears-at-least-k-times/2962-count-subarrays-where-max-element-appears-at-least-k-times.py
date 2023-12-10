class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        result = 0
        m=max(nums)
        freq=0
        left=0
        for right in range(n):
            if nums[right]==m:
                freq+=1
            while freq>=k:
                result += n-right 
                if nums[left]==m:
                    freq-=1
                left+=1
        return result
