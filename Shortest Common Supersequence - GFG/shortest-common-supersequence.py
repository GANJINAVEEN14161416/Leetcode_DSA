#User function Template for python3

class Solution:
    
    #Function to find length of shortest common supersequence of two strings.
    def shortestCommonSupersequence(self, s1,s2,x,y):
        dp=[[0]*(y+1) for i in range(x+1)]
        for ind1 in range(1,x+1):
            for ind2 in range(1,y+1):
                if s1[ind1-1]==s2[ind2-1]:
                    dp[ind1][ind2]=1+ dp[ind1-1][ind2-1]
                else:
                    dp[ind1][ind2]=max(dp[ind1-1][ind2],dp[ind1][ind2-1])
        return x+y-dp[-1][-1]
         #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        X,Y=input().split()
        
        print(Solution().shortestCommonSupersequence(X,Y,len(X),len(Y)))
        
# } Driver Code Ends