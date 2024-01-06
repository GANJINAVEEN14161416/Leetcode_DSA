class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans=0
        for i in range(32):
            temp=0
            x=1<<i
            for k in range(len(nums)):
                if nums[k]&x:
                    temp+=1
            if temp%3!=0:
                ans=ans|x
                #print(ans)
        return ans if ans < (1<<31) else ans-(1<<32)
        