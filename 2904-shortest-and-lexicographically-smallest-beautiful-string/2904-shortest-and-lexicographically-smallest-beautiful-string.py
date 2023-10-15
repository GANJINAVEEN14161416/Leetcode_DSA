class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n=len(s)
        ans="1"*n
        flag=False
        for i in range(len(s)):
            for j in range(i,len(s)):
                if s[j]!="0" and s[i:j+1].count("1")==k:
                    flag=True
                    if int(ans)>int(s[i:j+1]) and s[j]!="0":
                        ans=str(int(s[i:j+1]))
                        
        l=s.count("0") # edge case for s="000" and k=3
        if l==n or not flag:
            return ""
        return ans
        
        