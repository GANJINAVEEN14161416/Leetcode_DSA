class Solution:
	def editDistance(self, word1, word2):
	    n = len(word1)
        m = len(word2)
        
        t = [[0 for p in range(0,m+1)]
            for q in range(0,n+1)]
        
        for a in range(0,n+1):
            t[a][0] = a
        for b in range(1,m+1):
            t[0][b] = b
            
        for i in range(1,n+1):
            for j in range(1,m+1):
                
                if word1[i-1] == word2[j-1]:
                    t[i][j] = t[i-1][j-1]
                    
                else:
                    t[i][j] = 1 + min(t[i][j-1], t[i-1][j], t[i-1][j-1])
                    
        return t[n][m]
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