#User function Template for python3
class Solution:

	def count(self,arr, n, x):
        fl,cl=n,n
        left,right=0,n-1
        while left<=right:
            mid=(left+right)//2
            if arr[mid]>=x:
                fl=mid
                right=mid-1
            else:
                left=mid+1
        left,right=0,n-1
        while left<=right:
            mid=(left+right)//2
            if arr[mid]>x:
                cl=mid
                right=mid-1
            else:
                left=mid+1
        if fl<=cl:
            return cl-fl
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