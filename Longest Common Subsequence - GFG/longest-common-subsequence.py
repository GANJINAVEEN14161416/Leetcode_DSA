#User function Template for python3

class Solution:
    def lcs(self,x,y,s1,s2):
        dp=[[0]*(y+1) for i in range(x+1)]
        for ind1 in range(1,x+1):
            for ind2 in range(1,y+1):
                if s1[ind1-1]==s2[ind2-1]:
                    dp[ind1][ind2]=1+ dp[ind1-1][ind2-1]
                else:
                    dp[ind1][ind2]=max(dp[ind1-1][ind2],dp[ind1][ind2-1])
        return dp[-1][-1]
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        x,y = map(int,input().strip().split())
        s1 = str(input())
        s2 = str(input())
        ob=Solution()
        print(ob.lcs(x,y,s1,s2))
# } Driver Code Ends