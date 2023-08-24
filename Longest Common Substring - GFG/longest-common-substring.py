#User function Template for python3

class Solution:
    def longestCommonSubstr(self, text1, text2, n, m):
        dp=[[0]*(len(text2)+1) for i in range(len(text1)+1)]
        ans=0
        count=0
        for ind1 in range(1,len(text1)+1):
            for ind2 in range(1,len(text2)+1):
                if text1[ind1-1]==text2[ind2-1]:
                    dp[ind1][ind2]=1+dp[ind1-1][ind2-1]
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