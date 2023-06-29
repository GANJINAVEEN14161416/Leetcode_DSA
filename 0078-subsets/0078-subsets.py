class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def back(nums,ans,temp):
            ans.append(temp)
            for i in range(len(nums)):
                back(nums[i+1:],ans,temp+[nums[i]])
        ans=[]
        back(nums,ans,[])
        return ans
        