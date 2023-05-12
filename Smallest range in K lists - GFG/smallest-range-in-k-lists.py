#User function Template for python3
import heapq
class Solution:
    def smallestRange(self, KSortedArray, n, k):
        heap=[]
        maxvalue=0
        for i in range(k):
            heapq.heappush(heap,[KSortedArray[i][0],i,0])
            maxvalue=max(maxvalue,KSortedArray[i][0])
        heapq.heapify(heap)
        answer=[heap[0][0],maxvalue]
        while True:
            _,row,col=heapq.heappop(heap)
            if col==len(KSortedArray[row])-1:
                break
            next_num=KSortedArray[row][col+1]
            maxvalue=max(maxvalue,next_num)
            heapq.heappush(heap,[next_num,row,col+1])
            if maxvalue-heap[0][0]<answer[1]-answer[0]:
                answer=[heap[0][0],maxvalue]
        return answer


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t=int(input())
for _ in range(t):
    line=input().strip().split()
    n=int(line[0])
    k=int(line[1])
    numbers=[]
    for i in range(k):
        numbers.append([int(x) for x in input().strip().split()])
    r = Solution().smallestRange(numbers, n, k)
    print(r[0],r[1])
# } Driver Code Ends