#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        ans=1
        merge=[]
        for s,e in zip(start,end):
            merge.append([s,e])
        merge.sort(key=lambda x:x[1])
        stack=[merge[0]]
        for s,e in merge[1:]:
            if stack[-1][1]<s:
                ans+=1
                stack.append([s,e])
        return ans


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