#User function Template for python3

class Solution:
    def countSquares(self, N):
        if N==int((N**0.5))**2:
            return int(N**0.5)-1
        return int(N**0.5)
#User function Template for python3

# class Solution:
#     def countSquares(self, N):
#         import math
#         if int(N)==int(math.sqrt(N))**2:
#             return int(math.sqrt(N))-1
#         return int(math.sqrt(N))
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import math

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.countSquares(N))
# } Driver Code Ends