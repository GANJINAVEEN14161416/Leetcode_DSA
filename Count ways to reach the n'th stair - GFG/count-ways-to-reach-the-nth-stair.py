#User function Template for python3

class Solution:
    def countWays(self,n):
        pre1=1
        pre2=1
        for i in range(2,n+1):
            temp=pre1+pre2
            pre2=pre1
            pre1=temp
        return pre1%(10**9+7)



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
sys.setrecursionlimit(10**6)

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m = int(input())
        ob=Solution()
        print(ob.countWays(m))

# } Driver Code Ends