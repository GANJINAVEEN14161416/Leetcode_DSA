#User function Template for python3

class Solution:
    #Function to count number of ways to reach the nth stair.
    def countWays(self,n):
        dp=[-1]*(n+1)
        def solve(n):
            if n==0 or n==1:
                dp[n]=1
                return dp[n]
            if dp[n]!=-1:
                return dp[n]
            dp[n]=solve(n-1)+solve(n-2)
            return dp[n]
        return solve(n)%(10**9+7)


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
sys.setrecursionlimit(10**6)

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m = int(input())
        ob=Solution()
        print(ob.countWays(m))

# } Driver Code Ends