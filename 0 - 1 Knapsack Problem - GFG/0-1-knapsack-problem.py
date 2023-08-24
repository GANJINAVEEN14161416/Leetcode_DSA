#User function Template for python3

class Solution:
    def knapSack(self,W, wt, val, n):
        dp=[[-1]*(W+1) for i in range(n+1)]
        def solve(ind,target):
            if ind==0:
                if target>=wt[0]:
                    dp[ind][target]=val[0]
                    return val[0]
                dp[ind][target]=0
                return 0
            pick=not_pick=0
            if dp[ind][target]!=-1:
                return dp[ind][target]
            if target>=wt[ind]: # >=4
                pick=solve(ind-1,target-wt[ind])+val[ind]
            not_pick=solve(ind-1,target)
            dp[ind][target]=max(pick,not_pick)
            return max(pick,not_pick)
        return solve(n-1,W)
            
        
        
        
        
        
        
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends