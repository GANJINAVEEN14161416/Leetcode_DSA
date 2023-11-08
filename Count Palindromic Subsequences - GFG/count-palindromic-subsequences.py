class Solution:
    # Your task is to complete this function
    # Function should return an integer
    def countPS(self,s):
        # Code here
        n=len(s)
        mod=10**9+7
        dp=[[-1]*n for i in range(n)]
        def solve(ind1,ind2):
            if ind1==ind2:
                dp[ind1][ind2]=1
                return 1
            if ind1>ind2:
                dp[ind1][ind2]=0
                return 0
            if dp[ind1][ind2]!=-1:
                return dp[ind1][ind2]
            if s[ind1]==s[ind2]:
                dp[ind1][ind2]=(1+solve(ind1+1,ind2)+solve(ind1,ind2-1))%mod
                return dp[ind1][ind2]
            else:
                dp[ind1][ind2]=(solve(ind1+1,ind2)+solve(ind1,ind2-1)-solve(ind1+1,ind2-1))%mod
                return dp[ind1][ind2]
        return solve(0,n-1)



#{ 
 # Driver Code Starts
#Initial template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        ob=Solution()
        print(ob.countPS(input().strip()))

# } Driver Code Ends