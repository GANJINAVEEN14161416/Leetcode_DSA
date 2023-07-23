from typing import List
import heapq

class Solution:
    def kthLargest(self, N : int, k : int, arr : List[int]) -> int:
        # code here
        list1=[]
        for i in range(N):
            nums=arr[i]
            list1.append(nums)
            for j in range(i+1,N):
                nums+=arr[j]
                list1.append(nums)
        x=heapq.nlargest(k,list1)[-1]
        return x
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