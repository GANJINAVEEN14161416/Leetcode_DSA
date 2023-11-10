from typing import List

import heapq
class Solution:
    def kthLargest(self, N : int, k : int, arr : List[int]) -> int:
        # code here
        res=[]
        for i in range(N):
            c=arr[i]
            res.append(c)
            for j in range(i+1,N):
                c+=arr[j]
                res.append(c)
        return heapq.nlargest(k,res)[-1]
        



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
        
        
        K = int(input())
        
        
        Arr=IntArray().Input(N)
        
        obj = Solution()
        res = obj.kthLargest(N, K, Arr)
        
        print(res)
        

# } Driver Code Ends