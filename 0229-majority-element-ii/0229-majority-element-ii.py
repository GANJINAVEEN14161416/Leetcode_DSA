class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic=Counter(nums)
        n,list1=len(nums),[]
        for i,v in dic.items():
            if v>n//3:
                list1.append(i)
        return list1
        
        