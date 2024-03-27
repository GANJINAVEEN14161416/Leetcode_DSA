class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ans=0
        left=0
        n=len(nums)
        count=0
        nice=0
        for right in range(n):
            if nums[right]%2==1:
                count+=1
                nice=0
            while count==k:
                if nums[left]%2==1:
                    count-=1
                nice+=1
                left+=1
                print(left)
            ans+=nice
        return ans