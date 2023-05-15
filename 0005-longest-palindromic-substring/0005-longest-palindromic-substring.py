class Solution:
    def longestPalindrome(self, s: str) -> str:
        output=""
        n=len(s)
        count=0
        for i in range(n):
            left,right=i,i
            while left>=0 and right<n and s[right]==s[left]:
                if (right-left+1)>count:
                    count=right-left+1
                    output=s[left:right+1]
                left-=1
                right+=1
            left,right=i,i+1
            while left>=0 and right<n and s[left]==s[right]:
                if (right-left+1)>count:
                    count=right-left+1
                    output=s[left:right+1]
                left-=1
                right+=1
        return output