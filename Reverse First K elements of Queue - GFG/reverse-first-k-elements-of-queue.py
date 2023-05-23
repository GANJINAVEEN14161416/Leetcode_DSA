
def modifyQueue(q,k):
    def rev(q,k):
        if len(q)==0 or k<=0:
            return 
        pop=q.pop(0)
        rev(q,k-1)
        q.append(pop)
    rev(q,k)
    for i in range(len(q)-k):
        pop=q.pop(0)
        q.append(pop)
    return q


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

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
        a = list(map(int,input().strip().split()))

        queue = [] # our queue to be used
        for i in range(n):
            queue.append(a[i]) # enqueue elements of array in our queue

        print(*modifyQueue(queue,k))
# } Driver Code Ends