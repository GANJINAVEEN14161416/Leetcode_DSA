#User function Template for python3
class Solution:
	def minDifference(self, arr, n):
		total_sum = sum(arr)

        dp = [[False]*(total_sum+1) for i in range(n+1)]
        for i in range(n+1):
            dp[i][0] = True

        for i in range(1, n+1):
            for j in range(1, total_sum+1):
                if arr[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]

        min_diff = float('inf')
        for j in range(total_sum//2+1):
            if dp[n][j]:
                min_diff = min(min_diff, total_sum -2*j)
        return min_diff


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