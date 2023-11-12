
from typing import List
class Solution:
    def isStackPermutation(self, N : int, A : List[int], B : List[int]) -> int:
        # code here
        i,j,stack=0,0,[]
        for i in range(N):
            stack.append(A[i])
            while stack and stack[-1]==B[j]:
                pop=stack.pop()
                j+=1
        if j==N:
            return 1
        return 0
        




#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N = int(input())
        
        
        A=IntArray().Input(N)
        
        
        B=IntArray().Input(N)
        
        obj = Solution()
        res = obj.isStackPermutation(N, A, B)
        
        print(res)
        

# } Driver Code Ends