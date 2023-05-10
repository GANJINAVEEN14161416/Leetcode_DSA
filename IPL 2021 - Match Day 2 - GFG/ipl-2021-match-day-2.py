#User function Template for python3

class Solution:
    def max_of_subarrays(self,arr,n,k):
        stack,list1=[],[]
        for i,v in enumerate(arr):
            while stack and i-stack[0][0]>=k:
                stack=stack[1:]
            while stack and stack[-1][1]<v:
                stack.pop()
            stack.append([i,v])
            if i>=k-1:
                list1.append(stack[0][1])
        return list1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import deque

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,k = map(int,input().strip().split())
        arr = list(map(int,input().strip().split()))
        ob=Solution()
        res = ob.max_of_subarrays(arr,n,k)
        for i in range (len (res)):
            print (res[i], end = " ")
        print()
# } Driver Code Ends