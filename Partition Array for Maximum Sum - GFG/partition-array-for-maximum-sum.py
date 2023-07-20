#User function Template for python3

class Solution:
    def solve(self, n, k, arr):
        # Code here
        dp=[-1]*(n+1)
        for i in range(n-1,-1,-1):
            length=0
            maxi=float('-inf')
            ans=float('-inf')
            for j in range(i,min(i+k,n)):
                length+=1
                maxi=max(maxi,arr[j])
                add=length*maxi+dp[j+1]
                ans=max(ans,add)
            dp[i]=ans
        return dp[0]+1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n,k=input().split()
        n=int(n)
        k=int(k)
        arr= list(map(int, input().split()))
        ob = Solution()
        print(ob.solve(n, k, arr))
# } Driver Code Ends