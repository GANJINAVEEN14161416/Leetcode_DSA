#User function Template for python3

class Solution:
    def isSubsetSum (self, n, arr, W):
        t=[[False]*(W+1) for i in range(N+1)]
        for i in range(n+1):
            t[i][0]=True
        for i in range(1,n+1):
            for j in range(1,W+1):
                if arr[i-1]<=j:
                    t[i][j]=t[i-1][j-arr[i-1]] or t[i-1][j]
                else:
                    t[i][j]=t[i-1][j]
        return t[-1][-1]
                
        
        
        
        
        
        
        
        
        
        


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