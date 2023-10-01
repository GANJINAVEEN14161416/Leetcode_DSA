class Solution:
    def reverseWords(self, s: str) -> str:
        ans=""
        for word in s.split():
            ans+=word[::-1]+" "
        return ans[:-1]
        