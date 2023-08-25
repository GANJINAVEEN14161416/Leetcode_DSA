class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def isPredecessor(word1, word2):
            if abs(len(word1)-len(word2))!=1: 
                return False
            i,j=0,0
            n1,m1=len(word1),len(word2)
            n=len(word1)
            m=len(word2)
            while i<n1 and j<m1:
                if word1[i]==word2[j]:
                    i+=1
                    n-=1
                    m-=1
                    j+=1
                else:
                    i+=1
            return (n==1 and m==0)
        
        words.sort(key=len)
        n = len(words)
        dp = [1] * n
        ans = 1
        for i in range(1, n):
            for j in range(i):
                if isPredecessor(words[i], words[j]) and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
            ans = max(ans, dp[i])
        return ans
                       