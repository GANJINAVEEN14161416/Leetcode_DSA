#User function Template for python3

class Solution:

    def findMinDiff(self, arr,N,M):
        arr.sort()
        ans=float('inf')
        left,right=0,M-1
        while right<N:
            ans=min(ans,arr[right]-arr[left])
            left+=1
            right+=1
        return ans
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        A = [int(x) for x in input().split()]
        M = int(input())


        solObj = Solution()

        print(solObj.findMinDiff(A,N,M))
# } Driver Code Ends