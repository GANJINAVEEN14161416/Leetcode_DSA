#User function Template for python3
import math
class Solution:
    #Function to return sum of count of set bits in the integers from 1 to n.
    def countSetBits(self,n):
        def count(n):
            if n<=1:
                return n
            power=int(math.log2(n))
            less=2**power
            digit=less//2*power
            c=n-less
            ans=(1+digit)+c + count(c)
            return ans
        return count(n)
            
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        ob=Solution()
        print(ob.countSetBits(int(input())))
# } Driver Code Ends