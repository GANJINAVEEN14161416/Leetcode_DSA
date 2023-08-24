#User function Template for python3

class Solution:
    def knapSack(self, n, W, val, wt):
        
        dp=[[0]*(W+1) for i in range(n+1)]
        for i in range(W+1):
            if W>=wt[0]:
                dp[0][W]=val[0]
            else:
                dp[0][W]=0
        for ind in range(1,n+1):
            for target in range(1,W+1):
                pick=not_pick=0
                if target>=wt[ind-1]: # >=4
                    pick=dp[ind][target-wt[ind-1]]+val[ind-1]
                not_pick=dp[ind-1][target]
                dp[ind][target]=max(pick,not_pick)
        return dp[n][W]
            
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, W = [int(x) for x in input().split()]
        val = input().split()
        for itr in range(N):
            val[itr] = int(val[itr])
        wt = input().split()
        for it in range(N):
            wt[it] = int(wt[it])
        
        ob = Solution()
        print(ob.knapSack(N, W, val, wt))
# } Driver Code Ends