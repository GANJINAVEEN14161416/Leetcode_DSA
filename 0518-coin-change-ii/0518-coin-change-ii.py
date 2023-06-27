class Solution:
    def change(self, W: int, wt: List[int]) -> int:
        n=len(wt)
        t=[[-1]*(W+1) for i in range(n+1)]
        for i in range(n+1):
            for j in range(W+1):
                if i==0 and j==0:
                    t[i][j]=-1
                elif j==0:
                    t[i][j]=1
                elif i==0:
                    t[i][j]=0
        for i in range(1,n+1):
            for j in range(1,W+1):
                if wt[i-1]<=j:
                    t[i][j]=t[i][j-wt[i-1]]+t[i-1][j]
                else:
                    t[i][j]=t[i-1][j]
        return t[n][W]
        