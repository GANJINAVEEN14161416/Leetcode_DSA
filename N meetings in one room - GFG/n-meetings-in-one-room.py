#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        intervals=[]
        for i,j in zip(start,end):
            intervals.append([i,j])
        intervals.sort(key=lambda x:x[1])
        stack=[intervals[0]]
        for i,j in intervals[1:]:
            if stack[-1][1]<i:
                stack.append([i,j])
        return len(stack)
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends