class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summation=sum(nums)
        if summation%2==1:
            print(summation)
            return False
        def subset(arr,summ):
            prev=[False]*(summ+1)
            prev[0]=True
            N=len(arr)
            for ind in range(1,N+1):
                cur=[False]*(summ+1)
                cur[0]=True
                for target in range(1,summ+1):
                    nottake=prev[target]
                    take=False
                    if arr[ind-1]<=target:
                        take=prev[target-arr[ind-1]]
                    cur[target]=take or nottake
                prev=cur
            return prev[summ]  
        return subset(nums,summation//2)