class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ans=[]
        for i in nums:
            #i=2
            if i not in ans:
                ans.append(i)
        #nums=[1,1,2]
        nums[::]=ans[::]
        #nums=ans
        #nums=[1,2]
        return len(nums)
        
        
        