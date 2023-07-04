class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic={}
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        
        n,list1=len(nums),[]
        for i,v in dic.items():
            if v>n//3:
                list1.append(i)
        return list1
        
        