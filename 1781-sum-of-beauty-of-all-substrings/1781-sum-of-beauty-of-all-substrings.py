class Solution:
    def beautySum(self, s: str) -> int:
        n,count=len(s),0
        for  i in range(n):
            freq=[0]*26
            for j in range(i,n):
                freq[ord(s[j])-97]+=1
                count+=max(freq)-(min(x  for x in freq if x))
        return count
        