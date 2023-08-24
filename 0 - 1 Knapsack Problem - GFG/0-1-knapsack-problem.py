#User function Template for python3

class Solution:
    def knapSack(self,W, wt, val, n):
        prev=[0]*(W+1)
        for i in range(W+1):
            if W>=wt[0]:
                prev[W]=val[0]
        for ind in range(1,n+1):
            cur=[0]*(W+1)
            for target in range(1,W+1):
                pick=not_pick=0
                if target>=wt[ind-1]: # >=4
                    pick=prev[target-wt[ind-1]]+val[ind-1]
                not_pick=prev[target]
                cur[target]=max(pick,not_pick)
            prev=cur
        return prev[W]
            
        
        
        
        
        
        
        



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