#User function Template for python3

class Solution:
    def findTargetSumWays(self, arr, n, target):
        x=sum(arr)
        if target>x or (x-target)%2==1:
            return 0
        def subset(arr,W,n):
            mod=10**9+7
            t=[[0]*(W+1) for i in range(n+1)]
            for i in range(n+1):
                t[i][0]=1
            for i in range(1,n+1):
                for j in range(W+1):
                    if arr[i-1]<=j:
                        t[i][j]=(t[i-1][j-arr[i-1]] + t[i-1][j])%mod
                    else:
                        t[i][j]=t[i-1][j]%mod
            return t[-1][-1]
        return subset(arr,(x-target)//2,n)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        target = int(input())
        ob = Solution()
        print(ob.findTargetSumWays(arr,N, target))
# } Driver Code Ends