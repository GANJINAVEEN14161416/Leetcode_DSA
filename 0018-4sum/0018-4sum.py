class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=set()
        n=len(nums)
        nums.sort()
        for i in range(n-3):
            for j in range(i+1,n-2):
                k=j+1
                l=n-1
                while k<l:
                    temp=nums[i]+nums[j]+nums[k]+nums[l]
                    if temp==target:
                        ans.add((nums[i],nums[j],nums[k],nums[l]))
                        k+=1
                    elif temp>target:
                        l-=1
                    else:
                        k+=1
        return list(ans)
        