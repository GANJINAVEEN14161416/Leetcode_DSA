class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m=len(triangle)
        nxt=[0]*m
        for ind1 in range(m-1,-1,-1):
            cur=[0]*m
            for ind2 in range(ind1,-1,-1):
                if ind1==(m-1):
                    cur[ind2]=triangle[ind1][ind2]
                else:
                    downleft_diag=triangle[ind1][ind2]+nxt[ind2]
                    downright_diag=triangle[ind1][ind2]+nxt[ind2+1]
                    cur[ind2]=min(downleft_diag,downright_diag)
            nxt=cur
        return nxt[0]