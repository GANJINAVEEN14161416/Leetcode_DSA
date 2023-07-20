#User function Template for python3

class Solution:
    def matrixMultiplication(self, N, arr):
        t=[[-1]*N for i in range(N)]
        for i in range(1,N):
            t[i][i]=0
        for i in range(N-1,0,-1):
            for j in range(i+1,N):
                mini=float('inf')
                for k in range(i,j):
                    steps=arr[i-1]*arr[k]*arr[j]+t[i][k]+t[k+1][j]
                    if steps<mini:
                        mini=steps
                t[i][j]=mini
        return t[1][N-1]
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.matrixMultiplication(N, arr))
# } Driver Code Ends