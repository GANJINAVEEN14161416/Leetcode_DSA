class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic1=defaultdict(int)
        dic2=defaultdict(int)
        for i,j in zip(s,t):
            if (i in dic1 and dic1[i]!=j) or (j in dic2 and dic2[j]!=i):
                return False
            dic1[i]=j
            dic2[j]=i
        return True
            
        