class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        ans=0
        for n in nums:
            if n-1 in nums:
                continue
            nxt=n
            while (nxt+1) in nums:
                nxt+=1
            ans=max(ans,nxt-n+1)
        return ans