#User function Template for python3

class Solution:
    def isSubsetSum (self, N, arr, sum):
        # code here
        dp=[[-1]*(sum+1) for i in range(N+1)]
        for i in range(sum+1):
            dp[0][i]=False
        for i in range(N+1):
            dp[i][0]=True
        for ind in range(1,N+1):
            for target in range(1,sum+1):
                nottake=dp[ind-1][target]
                take=False
                if target>=arr[ind-1]:
                    take=dp[ind-1][target-arr[ind-1]]
                dp[ind][target]=take or nottake
        return dp[N][sum]
            
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(N,arr,sum)==True:
            print(1)
        else :
            print(0)
            
        

# } Driver Code Ends