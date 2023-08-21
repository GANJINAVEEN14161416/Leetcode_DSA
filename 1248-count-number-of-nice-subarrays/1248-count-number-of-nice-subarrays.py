class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[i]=0
        prefixsum=0
        dic=defaultdict(int)
        dic[0]=1
        ans=0
        for i in nums:
            if i%2==1:
                prefixsum+=1
            ans+=dic[prefixsum-k]
            dic[prefixsum]+=1
        return ans