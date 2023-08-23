#User function Template for python3

class Solution:
    def isSubsetSum (self, N, arr, sum):
        # code here
        dp=[[-1]*(sum+1) for i in range(N+1)]
        def solve(ind,target):
            if ind==0:
                if arr[ind]==target:
                    dp[ind][target]=True
                else:
                    dp[ind][target]=False
                return dp[ind][target]
            if target==0:
                dp[ind][target]=True
                return dp[ind][target]
            if dp[ind][target]!=-1:
                return dp[ind][target]
            nottake=solve(ind-1,target)
            take=False
            if target>=arr[ind]:
                take=solve(ind-1,target-arr[ind])
            dp[ind][target]=take or nottake
            return take or nottake
        return solve(N-1,sum)
            
        
        


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