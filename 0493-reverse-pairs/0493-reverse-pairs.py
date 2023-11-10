class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        ans,n=[0]*1,len(nums)
        def mergesort(nums):
            if len(nums)>1:
                mid=len(nums)//2
                left_nums=nums[:mid]
                right_nums=nums[mid:]
                mergesort(left_nums)
                mergesort(right_nums)
                i=j=0
                for i in range(len(left_nums)):
                    while j<len(right_nums) and  left_nums[i]>2*right_nums[j] :
                        j+=1
                    ans[0]+=j
                i=k=j=0
                while i<len(left_nums) and j<len(right_nums):
                    if left_nums[i]<right_nums[j]:
                        nums[k]=left_nums[i]
                        i+=1
                    else:
                        nums[k]=right_nums[j]
                        j+=1
                    k+=1
                while i<len(left_nums):
                    nums[k]=left_nums[i]
                    i+=1
                    k+=1
                while j<len(right_nums):
                    nums[k]=right_nums[j]
                    j+=1
                    k+=1
        mergesort(nums)
        return ans[0]
                    
                