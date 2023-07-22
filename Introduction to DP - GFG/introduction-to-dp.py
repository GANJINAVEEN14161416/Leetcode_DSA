#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def topDown(self, n):
        dp=[0]*(n+1)
        dp[0]=0
        dp[1]=1
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]%(10**9+7)
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