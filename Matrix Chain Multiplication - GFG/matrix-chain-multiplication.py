#User function Template for python3

class Solution:
    def matrixMultiplication(self, N, arr):
        t=[[-1]*N for i in range(N)]
        def solve(arr,i,j):
            if i>=j:
                return 0
            if t[i][j]!=-1:
                return t[i][j]
            mini=float('inf')
            for k in range(i,j):
                steps=arr[i-1]*arr[k]*arr[j]+solve(arr,i,k)+solve(arr,k+1,j)
                if steps<mini:
                    mini=steps
            t[i][j]=mini
            return mini
        return solve(arr,1,N-1)
        
            
        
        
    #     dp=[[-1]*N for _ in range(N)]
    #     return self.solve(1,N-1,arr,dp)
    
    # def solve(self,i,j,arr,dp):
    #     if i>=j:
    #         return 0
    #     if dp[i][j]!=-1:
    #         return dp[i][j]
            
    #     temp=float('inf')
    #     for k in range(i,j):
    #         ans=self.solve(i,k,arr,dp)+self.solve(k+1,j,arr,dp)+arr[i-1]*arr[k]*arr[j]
    #         temp=min(temp,ans)
    #     dp[i][j]=temp
    #     return temp


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