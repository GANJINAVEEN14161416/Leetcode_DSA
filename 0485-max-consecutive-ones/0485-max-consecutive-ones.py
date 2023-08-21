class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans=0
        count=0
        dic=defaultdict(int)
        for i in nums:
            if i==1:
                count+=1
            else:
                count=0
            ans=max(ans,count)
        return ans
        
        