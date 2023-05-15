class Solution:
    # Your task is to complete this function
    # Function should return an integer
    def countPS(self,s):
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(i, -1, -1):
                if i == j:
                    dp[j][i] = 1
                else:
                    if s[i] == s[j]:
                        dp[j][i] = dp[j+1][i] + dp[j][i-1] + 1
                    else:
                        dp[j][i] = dp[j+1][i] + dp[j][i-1] - dp[j+1][i-1]
        return dp[0][n-1]%(10**9+7)
    

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