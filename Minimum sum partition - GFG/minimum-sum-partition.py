#User function Template for python3
class Solution:
	def minDifference(self, arr, n):
	    x=sum(arr)
        def subset(N,arr,W):
            x=sum(arr)
            dp=[[False]*(W+1) for i in range(N+1)]
            for i in range(N+1):
                dp[i][0]=True
            for i in range(1,N+1):
                for j in range(1,W+1):
                    if arr[i-1]>j:
                        dp[i][j]=dp[i-1][j]
                    else:
                        dp[i][j]=(dp[i-1][j-arr[i-1]] or dp[i-1][j])
            ans=float('inf')
            for i in range(W+1):
                if dp[n][i]:
                    ans=min(ans,x-2*i)
            return ans
        return subset(N,arr,x//2)
        
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minDifference(arr, N)
		print(ans)

# } Driver Code Ends