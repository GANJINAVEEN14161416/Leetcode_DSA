class Solution:
    # Your task is to complete this function
    # Function should return an integer
    def countPS(self,s):
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1  # Single characters are palindromes
    
        for length in range(2, n + 1):
            for i in range(n - length, -1, -1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j] + dp[i][j - 1] + 1  # Include both ends and count unique palindromes
                else:
                    dp[i][j] = dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]  # Exclude either end once
    
        return dp[0][n - 1]%(10**9+7)
    
        

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