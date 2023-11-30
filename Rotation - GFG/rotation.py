#User function Template for python3
class Solution:
    def findKRotation(self,arr,  n):
        # code here
        left=0
        right=n-1
        ans=1e9
        index=-1
        while left<=right:
            mid=(left+right)//2
            if arr[left]<=arr[mid]:
                if ans>arr[left]:
                    ans=arr[left]
                    index=left
                left=mid+1
            else:
                if ans>arr[mid]:
                    ans=arr[mid]
                    index=mid
                right=mid-1
        return index
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

	tc=int(input())
	while tc > 0:
		n=int(input())
		a=list(map(int , input().strip().split()))
		ob = Solution()
		ans=ob.findKRotation(a, n)
		print(ans)
		tc=tc-1



# } Driver Code Ends