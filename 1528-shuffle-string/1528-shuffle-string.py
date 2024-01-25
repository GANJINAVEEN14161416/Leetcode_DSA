class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        list1=[""]*len(s)
        for i,j in enumerate(indices):
            list1[j]=s[i]
        return "".join(list1)
      