class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dic=defaultdict(int)
        n=len(nums)
        for i in nums:
            dic[i]+=1
            if dic[i]==2:
                rep=i
                break
        miss=list(set(list(range(1,n+1)))-set(nums))[0]
        return [rep,miss]
        
        