class Solution:
    def isSubsequence(self, A: str, B: str) -> bool:
        if not A:
            return True
        j=0
        for i in range(len(B)):
            if(A[j]==B[i]):
                j+=1
            if(j==len(A)):
                return True
        return False
