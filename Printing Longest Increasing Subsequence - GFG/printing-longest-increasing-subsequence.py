#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def longestIncreasingSubsequence(self, n, arr):
        lis=[1]*(n)
        hash=[0]*n
        lastind=0
        mx=1
        for i in range(n):
            hash[i]=i
            for j in range(0,i):
                if arr[i]>arr[j] and lis[i]<1+lis[j]:
                    lis[i]=1+lis[j]
                    hash[i]=j
            if lis[i]>mx:
                mx=lis[i]
                lastind=i
        
        temp=[]
        temp.append(arr[lastind])
        while hash[lastind]!=lastind:
            lastind=hash[lastind]
            temp.append(arr[lastind])
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