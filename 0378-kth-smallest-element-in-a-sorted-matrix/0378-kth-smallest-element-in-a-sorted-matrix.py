class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        list1=[]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                list1.append(matrix[r][c])
        list1.sort()              
        return list1[k-1]
        