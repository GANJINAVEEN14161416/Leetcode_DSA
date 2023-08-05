class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        count=0
        dup=len(set(nums))
        n=len(nums)
        for i in range(n-dup+1):
            s=set()
            for j in range(i,n):
                s.add(nums[j])
                if len(s)==dup:
                    count+=1
        return count
                    