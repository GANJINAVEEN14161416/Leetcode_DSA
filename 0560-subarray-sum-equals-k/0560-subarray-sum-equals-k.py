class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix=ans=0
        dic=defaultdict(int)
        dic[0]=1
        for i in nums:
            prefix+=i
            ans+=dic[prefix-k]
            dic[prefix]+=1
        return ans
        