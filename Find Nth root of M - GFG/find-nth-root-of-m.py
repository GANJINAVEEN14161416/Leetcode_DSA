#User function Template for python3

class Solution:
	def NthRoot(self, n, m):
    	left=0
		right=m
		while left<=right:
		    mid=(left+right)//2
		    if mid**n<=m:
		        left=mid+1
		    else:
		        right=mid-1
		if right**n==m:
		    return right      
        return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n); m = int(m);
		ob = Solution()
		ans = ob.NthRoot(n, m)
		print(ans)
# } Driver Code Ends