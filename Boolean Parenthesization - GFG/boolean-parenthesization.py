#User function Template for python3

class Solution:
    def countWays(self, N, S):
        mod=1003
        dp=[[[0 for i in range(2)]for i in range(N+2)]for i in range(N+2)]
        if N==1:
            if S[0]=="T":
                return 1
            else:
                return 0
        for i in range(N):
            dp[i][i][1]=S[i]=='T'
            dp[i][i][0]=S[i]=='F'
        #matrix chain multiplication
        for i in range(N,-1,-1):
            for j in range(1,N+1):
                if i>j:
                    continue
                #checking all possibilities
                for k in range(i+1,j,2):
                    lt=dp[i][k-1][1]
                    lf=dp[i][k-1][0]
                    rt=dp[k+1][j][1]
                    rf=dp[k+1][j][0]
                    #S[k]=="|" then calculate answer
                    if S[k]=="|":
                        dp[i][j][1]=(dp[i][j][1] + (lt*rt) +(lt*rf) +(lf*rt))%mod  #if expression is true
                        dp[i][j][0]=(dp[i][j][0] + (lf*rf))%mod  #if expression is false
                    #S[k]=="&" then calculate answer
                    elif S[k]=="&":
                        dp[i][j][1]=(dp[i][j][1]+ (lt*rt))%mod    #if expression is true
                        dp[i][j][0]=(dp[i][j][0] + (lt*rf) + (lf*rt) + (lf*rf))%mod  #if expression is false
                    #S[k]=="^" then calculate answer   
                    else:
                        dp[i][j][1]=(dp[i][j][1]+ (lt*rf) + (lf*rt))%mod  #if expression is true
                        dp[i][j][0]=(dp[i][j][0] + (lt*rt) + (lf*rf))%mod   #if expression is false
        #return answer of string S start=0,end=N-1,expression = True     
        return dp[0][N-1][1]
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        S = input()
        
        ob = Solution()
        print(ob.countWays(N, S))
# } Driver Code Ends