class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=""
        for i,j in zip(word1,word2):
            res+=i
            res+=j
        m=min(len(word1),len(word2))
        if len(word1)>len(word2):
            res+=word1[m:]
        if len(word1)<len(word2):
            res+=word2[m:]
        return res
