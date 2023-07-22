#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
from sys import setrecursionlimit
setrecursionlimit(10**9)
class Solution:
    def topDown(self, n):
        dp=[-1]*(n+1)
        def solve(n):
            if n==0 or n==1:
                dp[n]=n
                return dp[n]
            if dp[n]!=-1:
                return dp[n]
            dp[n]=solve(n-1)+solve(n-2)
            return dp[n]
        return solve(n)%(10**9+7)
    def bottomUp(self, n):
        # Code here
        dp=[0]*(n+1)
        dp[0]=0
        dp[1]=1
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]%(10**9+7)
        
        
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n = int(input())
        ob = Solution()
        topDownans=ob.topDown(n);
        bottomUpans=ob.bottomUp(n);
        if(topDownans!=bottomUpans):
            print(-1)
        else:
            print(bottomUpans)
# } Driver Code Ends