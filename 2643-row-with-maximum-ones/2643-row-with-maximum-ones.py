class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        list1=[]
        for ind,row in enumerate(mat):
            list1.append([ind,row.count(1)])
        list1.sort(key=lambda x:[-x[1],x[0]])
        return list1[0]
                # return sorted([(ind,val.count(1)) for ind,val in enumerate(mat)],key=lambda x:[-x[1],x[0]])[0]
