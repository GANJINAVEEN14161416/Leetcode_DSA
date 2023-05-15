#User function Template for python3
import math
class Solution:
    #Function to return sum of count of set bits in the integers from 1 to n.
    def countSetBits(self,n):
        # if n <= 1:
        #     return n
        # # exponent of 2
        # a = math.log(n, 2)
        # a = int(a)
        # # (highest power of 2 less than the number)/2
        # b = 2 ** a // 2
        # # number-highest power of 2
        # c = n - 2 ** a
        # sol = (a * b + 1) + c + self.countSetBits(c)
        # return sol
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