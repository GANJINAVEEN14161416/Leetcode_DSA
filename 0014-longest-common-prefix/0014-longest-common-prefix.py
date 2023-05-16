class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        n=len(strs)
        strs.sort()
        for i in range(len(strs[0])):
            if strs[0][i]==strs[n-1][i]:
                ans+=strs[0][i]
            else:
                break
        return ans
            
        
        
        
#         if not strs:
#             return ""
#         short=min(strs,key=len)
#         for i,v in enumerate(short):
#             for w in strs:
#                 if w[i]!=short[i]:
#                     return short[:i]
#         return short 
        