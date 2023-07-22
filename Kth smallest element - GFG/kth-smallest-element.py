#User function Template for python3
import heapq
class Solution:
    def kthSmallest(self,arr, l, r, k):
        def heapify(arr, N, i):
         
            largest = i  # Initialize largest as root
            l = 2 * i + 1  # left = 2*i + 1
            r = 2 * i + 2  # right = 2*i + 2
         
            # If left child is larger than root
            if l < N and arr[l] < arr[largest]:
                largest = l
         
            # If right child is larger than largest so far
            if r < N and arr[r] < arr[largest]:
                largest = r
         
            # If largest is not root
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
         
                # Recursively heapify the affected sub-tree
                heapify(arr, N, largest)
        def buildHeap(arr, N):
            startIdx = N // 2 - 1
            for i in range(startIdx, -1, -1):
                heapify(arr, N, i)
        buildHeap(arr,len(arr))
        for i in range(len(arr)):
           x= heapq.heappop(arr)
           if i==(k-1):
               return x
        return x
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    import random 
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=list(map(int,input().strip().split()))
        k=int(input())
        ob=Solution()
        print(ob.kthSmallest(arr, 0, n-1, k))
        
# } Driver Code Ends