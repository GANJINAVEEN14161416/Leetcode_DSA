class Solution:
    def inversionCount(self, arr, n):
        return self.mergeSort(arr, n)
    def mergeSort(self, arr, n):
        if n < 2:
            return 0
        mid = n //2
        left = arr[:mid]
        right = arr[mid:]
        c = 0
        c += self.mergeSort(left, mid)
        c += self.mergeSort(right, n - mid)
        c += self.merge(arr, left, right, mid, n-mid)
        return c
    def merge(self, arr, left, right, mid, n):
        i=k=c=j=0
        while i < mid and j < n:
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                c += mid - i
                j += 1
            k += 1
        while i < mid:
            arr[k] = left[i]
            i += 1
            k += 1
        while j < n:
            arr[k] = right[j]
            j += 1
            k += 1
        
        return c
    
                    
                    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a,n))
# } Driver Code Ends