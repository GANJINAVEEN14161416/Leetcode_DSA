class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        answer=max(nums)
        count=0
        for n in nums:
            if count<0:
                count=0
            count+=n
            answer=max(answer,count)
        return answer

        