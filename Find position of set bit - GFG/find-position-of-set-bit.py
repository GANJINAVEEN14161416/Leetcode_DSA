#User function Template for python3
import math
class Solution:
    def findPosition(self, N):
        if bin(N).count("1")>1 or N==0:
            return -1
        return int(math.log2(N)+1)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        
        ob = Solution()
        print(ob.findPosition(N))
# } Driver Code Ends