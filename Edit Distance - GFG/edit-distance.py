class Solution:
	def editDistance(self, s, t):
        dp=[[float("inf")]*(len(t)+1) for i in range(len(s)+1)]
        for k in range(len(s)+1):
            dp[k][len(t)]=len(s)-k
        for k in range(len(t)+1):
            dp[len(s)][k]=len(t)-k
        for i in range(len(s)-1,-1,-1):
            for j in range(len(t)-1,-1,-1):
                if s[i]==t[j]:
                    dp[i][j]=dp[i+1][j+1]
                else:
                    dp[i][j]=1+min(dp[i+1][j+1],dp[i+1][j],dp[i][j+1])
        return dp[0][0]

#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s, t = input().split()
		ob = Solution();
		ans = ob.editDistance(s, t)
		print(ans)
# } Driver Code Ends