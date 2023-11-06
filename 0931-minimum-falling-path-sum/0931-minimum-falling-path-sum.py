class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        nxt=matrix[n-1]
        for ind1 in range(n-2,-1,-1):
            cur=[0]*n
            for ind2 in range(n-1,-1,-1):
                left,right,below=float('inf'),float('inf'),float('inf')
                if ind1+1<n and ind2-1>=0:
                    left=nxt[ind2-1]+matrix[ind1][ind2]
                if ind1+1<n:
                    below=nxt[ind2]+matrix[ind1][ind2]
                if ind1+1<n and ind2+1<n:
                    right=nxt[ind2+1]+matrix[ind1][ind2]
                cur[ind2]=min(left,right,below)
            nxt=cur
        return min(nxt)
        