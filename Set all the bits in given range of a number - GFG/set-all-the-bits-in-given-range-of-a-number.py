#User function Template for python3

class Solution:
    def setAllRangeBits(self, N , L , R):
        # code here 
        for i in range(L-1,R):
            N=N | 1<<i
        return N


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,L,R=map(int,input().split())
        
        ob = Solution()
        print(ob.setAllRangeBits(N,L,R))
# } Driver Code Ends