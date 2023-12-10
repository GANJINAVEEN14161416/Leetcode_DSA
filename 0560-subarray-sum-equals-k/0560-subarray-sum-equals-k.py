class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic=defaultdict(int)
        dic[0]=1
        prefix=0
        ans=0
        for i in nums:
            prefix+=i
            ans+=dic[prefix-k]
            dic[prefix]+=1
        return ans