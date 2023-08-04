class Solution:
    def reverseWords(self, s: str) -> str:
        list1=[]
        for w in s.split():
            list1.append(w)
        ans= " ".join(list1[::-1])
        return ans
        