class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        m=len(matrix[0])
        prev=[0]*(len(matrix[0]))
        for ind2 in range(m):
            prev[ind2]=matrix[0][ind2]
        for ind1 in range(1,n):
            cur=[0]*(m+1)
            for ind2 in range(m):
                left=float('inf')
                if ind1-1>=0 and ind2-1>=0:
                    left=matrix[ind1][ind2]+prev[ind2-1]
                up=float('inf')
                if ind1-1>=0:
                    up=matrix[ind1][ind2]+prev[ind2]
                right=float('inf')
                if ind2+1<len(matrix[0]) and ind1-1>=0:
                    right=matrix[ind1][ind2]+prev[ind2+1]
                cur[ind2]=min(left,up,right)
            prev=cur
        ans=float('inf')
        for i in range(n):
            ans=min(ans,prev[i])
        return ans
                