class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans=0
        count=0
        for i in nums:
            if count==0:
                ans=i
            if ans==i:
                count+=1
            else:
                count-=1
        return ans
        

        
        