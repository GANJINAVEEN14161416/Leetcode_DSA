#User function Template for python3

class Solution:
    def count(self, wt, n, W):
        t=[[-1]*(W+1) for i in range(n+1)]
        for i in range(n+1):
            for j in range(W+1):
                if j==0:
                    t[i][j]=1
                elif i==0:
                    t[i][j]=0
        for i in range(1,n+1):
            for j in range(1,W+1):
                if wt[i-1]<=j:
                    t[i][j]=t[i][j-wt[i-1]]+t[i-1][j]
                else:
                    t[i][j]=t[i-1][j]
        return t[n][W]





#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        sum,N = list(map(int, input().strip().split()))
        coins = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.count(coins,N,sum))

# } Driver Code Ends