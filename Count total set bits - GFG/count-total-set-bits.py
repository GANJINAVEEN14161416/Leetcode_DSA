#User function Template for python3
import math
class Solution:
    #Function to return sum of count of set bits in the integers from 1 to n.
    def countSetBits(self,n):
        def count(n):
            if n<=0:
                return n
            less=int(math.log2(n))
            x=((2**less)//2)*less
            c=n-(2**less)
            return x+c+1+count(c)
        return count(n)
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        ob=Solution()
        print(ob.countSetBits(int(input())))
# } Driver Code Ends