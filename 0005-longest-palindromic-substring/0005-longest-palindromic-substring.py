class Solution:
    def longestPalindrome(self, s: str) -> str:
            n = len(s)
            if n < 2:
                return s

            start, end = 0, 0
            for i in range(n):
                # check for odd-length palindromes
                l, r = i, i
                while l >= 0 and r < n and s[l] == s[r]:
                    l -= 1
                    r += 1
                if r - l - 1 > end - start:
                    start, end = l + 1, r

                # check for even-length palindromes
                l, r = i, i+1
                while l >= 0 and r < n and s[l] == s[r]:
                    l -= 1
                    r += 1
                if r - l - 1 > end - start:
                    start, end = l + 1, r

            return s[start:end]
