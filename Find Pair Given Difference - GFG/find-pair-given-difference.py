#User function Template for python3

class Solution:

    def findPair(self, arr, L,N):
        arr.sort()
        for i,v in enumerate(arr):
            num=v+N
            if num in arr[i+1::]:
                return True
        return False
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        L,N = [int(x) for x in input().split()]
        arr = [int(x) for x in input().split()]

        solObj = Solution()

        if(solObj.findPair(arr,L, N)):
            print(1)
        else:
            print(-1)
# } Driver Code Ends