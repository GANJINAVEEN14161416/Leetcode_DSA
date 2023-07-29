
from bisect import insort, bisect_right
from typing import List
class Solution:
    def findLeastGreater(self, n : int, arr : List[int]) -> List[int]:
        ans=[-1]*n
        temp=[]
        for i in range(n-1,-1,-1):
            insort(temp,arr[i])
            index=bisect_right(temp,arr[i])
            if index<len(temp):
                ans[i]=temp[index]
        return ans
        



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
        
        n = int(input())
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.findLeastGreater(n, arr)
        
        IntArray().Print(res)
        

# } Driver Code Ends