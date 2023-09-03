class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordset=set(wordDict)
        n=len(s)
        dp=[False]*(n+1)
        dp[n]=True
        for ind1 in range(n-1,-1,-1):
            for end in range(ind1+1,n+1):
                word=s[ind1:end]
                if word in wordset and dp[end]:
                    dp[ind1]=True
        return dp[0]
        # def solve(ind1):
        #     if ind1==n:
        #         return True
        #     for end in range(ind1+1,n+1):
        #         word=s[ind1:end]
        #         if word in wordset and solve(end):
        #             return True
        #     return False
        # return solve(0)

#         @lru_cache(None)
#         def dp(start):
#             if start == n:  # Found a valid way to break words
#                 return True

#             for end in range(start + 1, n + 1):  # O(N^2)
#                 word = s[start:end]  # O(N)
#                 if word in wordSet and dp(end):
#                     return True
#             return False

#         return dp(0)
        