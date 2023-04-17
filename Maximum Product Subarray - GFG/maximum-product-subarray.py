#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr, n):
		# code here
		cmax=cmin=1
		count=max(arr)
		for m in arr:
		    temp=cmax*m
		    cmax=max(cmax*m,cmin*m,m)
		    cmin=min(temp,cmin*m,m)
		    count=max(count,cmax)
		return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends