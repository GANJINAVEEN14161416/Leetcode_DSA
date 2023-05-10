from typing import List


class Solution:
    def kthLargest(self, N : int, K : int, Arr : List[int]) -> int:
        list1=[]
        for i in range(N):
            num=0
            list1.append(Arr[i])
            num+=Arr[i]
            for j in range(i+1,N):
                num+=Arr[j]
                list1.append(num)
        list1.sort()
        return list1[-K]



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