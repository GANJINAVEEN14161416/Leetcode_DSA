#User function Template for python3

class Solution:
    def longestCommonSubstr(self, s1,s2, x, y):
        # code here
        ans=0
        dp=[[0]*(y+1) for i in range(x+1)]
        for ind1 in range(1,x+1):
            for ind2 in range(1,y+1):
                if s1[ind1-1]==s2[ind2-1]:
                    dp[ind1][ind2]=1+ dp[ind1-1][ind2-1]
                    ans=max(ans,dp[ind1][ind2])
                else:
                    dp[ind1][ind2]=0
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n,m = input().strip().split(" ")
        n,m = int(n), int(m)
        S1 = input().strip()
        S2 = input().strip()
        
        
        ob=Solution()
        print(ob.longestCommonSubstr(S1, S2, n, m))
# } Driver Code Ends