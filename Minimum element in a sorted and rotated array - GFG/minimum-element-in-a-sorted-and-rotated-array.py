#User function Template for python3
import heapq
class Solution:
    def findMin(self, arr, n):
        left,right=0,n-1
        while left<=right:
            mid=(left+right)//2
            prev=(mid-1)%n
            next=(mid+1)%n
            if arr[mid]<=arr[prev] and arr[mid]<=arr[next]:
                return arr[mid]
            elif arr[mid]<=arr[right]:
                right=mid-1
            elif arr[mid]>=arr[left]:
                left=mid+1

        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        print(ob.findMin(arr, n))
# } Driver Code Ends