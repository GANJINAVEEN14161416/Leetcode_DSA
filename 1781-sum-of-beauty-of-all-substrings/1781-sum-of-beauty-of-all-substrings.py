class Solution:
    def beautySum(self, s: str) -> int:
        ans=0
        n=len(s)
        for i in range(n):
            freq=[0]*26
            for j in range(i,n):
                freq[ord(s[j])-97]+=1
                mx=max(freq)
                mi=float('inf')
                for k in range(26):
                    if freq[k]:
                        mi=min(freq[k],mi)
                if mi!=float('inf'):
                    ans+=mx-mi
        return ans
                