class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def kthSmallest(mat, n, k): 
            # Your code goes here
            left,right=mat[0][0],mat[-1][-1]
            while left<=right:
                mid=(left+right)//2
                count=0
                for row in mat:
                    count+=counter(row,mid)
                if count<k:
                    left=mid+1
                else:
                    right=mid-1
            return left



        def counter(row,mid):
            i=0
            count=0
            while i<len(row) and row[i]<=mid:
                count+=1
                i+=1
            return count
        return kthSmallest(matrix,len(matrix),k)
