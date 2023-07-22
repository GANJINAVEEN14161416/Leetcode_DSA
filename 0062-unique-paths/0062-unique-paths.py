class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev =[0]*(n+1)
        for ind1 in range(1,m+1):
            cur=[0]*(n+1)
            for ind2 in range(n+1):
                if ind1==0 or ind2==0:
                    prev[0]=0
                if ind1==1 and ind2==1:
                    cur[1]=1
                else:
                    left=0
                    down=0
                    if ind1-1>=0:
                        left=prev[ind2]
                    if ind2-1>=0:
                        down=cur[ind2-1]
                    cur[ind2]=left+down
            prev=cur
        return prev[n]
            
        # def solve(ind1,ind2):
        #     if ind1==1 and ind2==1:
        #         return 1
        #     if ind1==0  or ind2==0:
        #         return 0
        #     if dp[ind1][ind2]!=-1:
        #         return dp[ind1][ind2]
        #     dp[ind1][ind2]=solve(ind1-1,ind2)+solve(ind1,ind2-1)
        #     return dp[ind1][ind2]
        # return solve(m,n)