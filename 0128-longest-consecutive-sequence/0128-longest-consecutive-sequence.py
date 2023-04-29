class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numset=set(nums)
        length=0
        for n in nums:
            if (n-1) not in numset:
                count=0
                while (n+count) in numset:
                    count+=1
                length=max(count,length)
        return length
        