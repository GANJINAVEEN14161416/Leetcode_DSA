#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def longestIncreasingSubsequence(self, n, arr):
        dp=[1]*(n)
        hash=[0]*n
        maxind=0
        mx=1
        for i in range(n):
            hash[i]=i
            for j in range(0,i):
                if arr[i]>arr[j] and 1+dp[j]>dp[i]:
                    dp[i]=1+dp[j]
                    hash[i]=j
            if dp[i]>mx:
                mx=dp[i]
                maxind=i
        
        temp=[]
        while hash[maxind]!=maxind:
            temp.append(arr[maxind])
            maxind=hash[maxind]
        temp.append(arr[maxind])
        return temp[::-1]
        
        
        



#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.longestIncreasingSubsequence(N, arr)
        for val in res:
            print(val, end =' ')
        print()
# } Driver Code Ends