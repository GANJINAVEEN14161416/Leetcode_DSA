class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dic=Counter(nums)
        n=len(nums)
        for i,j in dic.items():
            if j==2:
                rep=i
        miss=(n*(n+1))//2-(sum(nums)-rep)
        return [rep,miss]
        
        