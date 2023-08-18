#User function Template for python3

class Solution:
    def isSubsetSum (self, N, arr, sum):
        # code here 
        dp=[[-1]*(sum+1) for i in range(N+1)]
        def solve(index,target):
            if target==0:
                dp[index][target]=True
                return True
            elif dp[index][target]!=-1:
                return dp[index][target]
            elif target<0 or index<0:
                return False
            else:
                take=False
                if arr[index]<=target:
                    take=solve(index-1,target-arr[index])
                nottake=solve(index-1,target)
                dp[index][target]=take or nottake
                return dp[index][target]
        
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