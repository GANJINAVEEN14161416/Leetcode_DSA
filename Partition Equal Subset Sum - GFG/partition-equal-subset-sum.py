# User function Template for Python3

class Solution:
    def equalPartition(self, n, arr):
        def subset(N,arr,h):
            dp=[[False]*(h+1) for i in range(N+1)]
            for i in range(N+1):
                dp[i][0]=True
            for i in range(1,N+1):
                for j in range(1,h+1):
                    if arr[i-1]>j:
                        dp[i][j]=dp[i-1][j]
                    else:
                        dp[i][j]=(dp[i-1][j-arr[i-1]] or dp[i-1][j])
                        
            return dp[-1][-1]
        h=sum(arr)
        if h%2==1:
            return False
        return subset(N,arr,h//2)


    


#{ 
 # Driver Code Starts
# Initial Template for Python3

import sys
input = sys.stdin.readline
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for it in range(N):
            arr[it] = int(arr[it])
        
        ob = Solution()
        if (ob.equalPartition(N, arr) == 1):
            print("YES")
        else:
            print("NO")
# } Driver Code Ends