#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def maxChildren(self, N, M, greed, sz):
        # Code here
        ans=0
        greed.sort()
        sz.sort()
        i=0
        j=0
        while i<N and j<M:
            if sz[j]>=greed[i]:
                i+=1
                j+=1
                ans+=1
            else:
                j+=1
        return ans
        
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N, M = list(map(int, input().split()))
        greed = list(map(int, input().split()))
        sz = list(map(int, input().split()))
        ob = Solution()
        res = ob.maxChildren(N, M, greed, sz)
        print(res)
# } Driver Code Ends