class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans=0
        for i in range(32):
            x=1<<i
            temp=0
            for j in range(len(nums)):
                if nums[j]&x:
                    temp+=1
            if temp%3!=0:
                ans=ans|x
        return ans if ans < (1<<31) else ans-(1<<32)
        