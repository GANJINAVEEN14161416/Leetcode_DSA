#User function Template for python3
import heapq
class Solution:

	def kLargest(self,arr, n, k):
		heap=[]
		list1=[]
		for i in range(n):
		    heapq.heappush(heap,-arr[i])
		while k>0:
		    list1.append(-heapq.heappop(heap))
		    k-=1
		return list1


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.kLargest(arr, n, k)
        for x in ans:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends