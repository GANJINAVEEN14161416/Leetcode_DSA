#User function Template for python3

class Solution:
	def pushZerosToEnd(self,arr, n):
    	# code here
    	left=0
    	for right in range(len(arr)):
    	    if arr[right]!=0:
    	        arr[right],arr[left]=arr[left],arr[right]
    	        left+=1
    	  


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
# } Driver Code Ends