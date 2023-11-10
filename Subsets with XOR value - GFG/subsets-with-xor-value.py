#User function Template for python3

import math
class Solution:
    def subsetXOR(self, arr, N, K): 
        dp=[[-1]*1000 for i in range(110)]
        def solve(ind,x):
            if ind<0:
                if x==K:
                    return 1
                return 0
            if dp[ind][x]!=-1:
                return dp[ind][x]
            nottake=solve(ind-1,x)
            take=solve(ind-1,x^arr[ind])
            dp[ind][x]=nottake+take
            return dp[ind][x]
        ans=solve(N-1,0)
        #solve(N-1,0).clear()
        return ans
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K = input().split()
        N = int(N)
        K = int(K)
        arr = input().split(' ')
        for itr in range(N):
            arr[itr] = int(arr[itr])
        ob = Solution()
        print(ob.subsetXOR(arr,N,K))
# } Driver Code Ends