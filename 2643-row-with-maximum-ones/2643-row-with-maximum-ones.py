class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        return sorted([(ind,val.count(1)) for ind,val in enumerate(mat)],key=lambda x:[-x[1],x[0]])[0]

        