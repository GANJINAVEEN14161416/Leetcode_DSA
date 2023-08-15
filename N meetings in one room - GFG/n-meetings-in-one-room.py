#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,s,e):
        meet=[]
        for i in range(n):
            meet.append([s[i],e[i],i+1])
        meet.sort(key=lambda x:x[1])
        ans=1
        last_time=meet[0][1]
        start_time=meet[0][0]
        for i in range(1,n):
            if meet[i][0]>last_time:
                ans+=1
                last_time=meet[i][1]
                start_time=meet[i][0]
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