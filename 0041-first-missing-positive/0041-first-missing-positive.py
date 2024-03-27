class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        dic=defaultdict(int)
        for i in nums:
            dic[i]+=1
        temp=list(range(1,10**5+1000))
        for i in temp:
            if not dic[i]:
                return i
        return -1
        
        