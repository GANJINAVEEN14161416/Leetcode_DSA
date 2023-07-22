class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n=len(obstacleGrid)
        m=len(obstacleGrid[0])
        prev=[0]*(m+1)
        cur=[0]*(m+1)
        for ind1 in range(1,n+1):
            for ind2 in range(1,m+1):
                if obstacleGrid[ind1-1][ind2-1]==1:
                    cur[ind2]=0
                else:
                    if ind1==1 and ind2==1:
                        cur[ind2]=1
                    else:
                        up,down=0,0
                        if ind1-1>=0:
                            up=prev[ind2]
                        if ind2-1>=0:
                            down=cur[ind2-1]
                        cur[ind2]=up+down
            prev=cur
        return prev[m]
                
        
        
        
        
#         def solve(ind1,ind2,obstacleGrid):
#             if obstacleGrid[ind1-1][ind2-1]==1:
#                 return 0
#             if dp[ind1][ind2]!=-1:
#                 return dp[ind1][ind2]
#             else:
#                 if ind1==0 or ind2==0:
#                     return 0
#                 if ind1==1 and ind2==1:
#                     return 1
#                 else:
#                     left=0
#                     down=0
#                     if ind1-1>=0:
#                         up=solve(ind1-1,ind2,obstacleGrid)
#                     if ind2-1>=0:
#                         down=solve(ind1,ind2-1,obstacleGrid)
#                     dp[ind1][ind2]=up+down
#                     return dp[ind1][ind2]
#         return solve(n,m,obstacleGrid)
        
        