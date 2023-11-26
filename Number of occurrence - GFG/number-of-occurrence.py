#User function Template for python3
class Solution:

	def count(self,arr, n, x):
		# code here
		def search(target):
		    left,right=0,n-1
		    while left<=right:
		        mid=(left+right)//2
		        if arr[mid]<target:
		            left=mid+1
		        else:
		            right=mid-1
		    return left
        l=search(x)
        r=search(x+1)-1
        if l<=r:
            return r-l+1
        return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.count(arr, n, x)
        print(ans)
        tc -= 1

# } Driver Code Ends