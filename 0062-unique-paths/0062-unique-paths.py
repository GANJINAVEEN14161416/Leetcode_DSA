class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev=[0]*(n+1)
        for ind1 in range(1,m+1):
            cur=[0]*(n+1)
            for ind2 in range(1,n+1):
                if ind1==ind2==1:
                    cur[ind2]=1
                else:
                    left=up=0
                    if ind2-1>=0:
                        left=cur[ind2-1]
                    if ind1-1>=0:
                        up=prev[ind2]
                    cur[ind2]=up+left
            prev=cur
        return cur[-1]