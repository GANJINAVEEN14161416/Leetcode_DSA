class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        temp1=(n*(n+1))//2-sum(nums)
        temp2=(n*(n+1)*(2*n+1))//6
        for i in nums:
            temp2-=i**2
        temp3=temp2//temp1
        miss=(temp1+temp3)//2
        dup=temp3-miss
        return [dup,miss]
        
        