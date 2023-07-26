class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dic={}
        def wordbreak(s):
            if s not in dic:
                ans=[]
                for w in wordDict:
                    if s[:len(w)]==w:
                        if len(s)==len(w):
                            ans.append(w)
                        else:
                            for word in wordbreak(s[len(w):]):
                                ans.append(w+" "+word)
                dic[s]=ans
            return dic[s]
        return wordbreak(s)
        