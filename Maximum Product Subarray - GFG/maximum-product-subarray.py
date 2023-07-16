#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr, n):
	    mi,mx=1,1
	    ans=max(arr)
	    for i in arr:
	        temp=mx*i
	        mx=max(mx*i,mi*i,i)
	        mi=min(temp,mi*i,i)
	        ans=max(ans,mx,mi)
	    return ans
	        


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