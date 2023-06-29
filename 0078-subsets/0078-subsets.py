class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        list1 = [[]]
        n=len(nums)
        for i in range(1,2**n):
            list2=[]
            for j in range(n):
                if (i&1<<j):
                    list2.append(nums[j])
            list1.append(list2)
        return list1
        