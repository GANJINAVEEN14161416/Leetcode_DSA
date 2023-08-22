class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        ans=[]
        for i in range(n-2):
            left=i+1
            right=n-1
            while left<right:
                number=nums[i]+nums[left]+nums[right]
                if number==0:
                    if [nums[i],nums[left],nums[right]] not in ans:
                        ans.append([nums[i],nums[left],nums[right]])
                    left+=1
                elif number>0:
                    right-=1
                else:
                    left+=1
        return ans
                
    
            
        