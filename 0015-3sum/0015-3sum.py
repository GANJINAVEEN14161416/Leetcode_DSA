class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n,ans=len(nums),[]
        nums.sort()
        for i in range(n-2):
            left=i+1
            right=n-1
            while left<right:
                val=nums[left]+nums[right]+nums[i]
                temp=[nums[i],nums[left],nums[right]]
                if val==0 and temp not in ans:
                    ans.append(temp)
                    left+=1
                elif val>0:
                      right-=1
                else:
                      left+=1
        return ans
                    