#User function Template for python3

class Solution:
    def isSubsetSum (self, N, arr, sum):
        # code here
        prev=[False]*(sum+1)
        prev[0]=True
        for ind in range(1,N+1):
            cur=[False]*(sum+1)
            cur[0]=True
            for target in range(1,sum+1):
                nottake=prev[target]
                take=False
                if target>=arr[ind-1]:
                    take=prev[target-arr[ind-1]]
                cur[target]=take or nottake
            prev=cur
        return prev[sum]
            
        
        


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