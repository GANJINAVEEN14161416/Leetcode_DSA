class Solution:
    def maxSlidingWindow(self, arr: List[int], k: int) -> List[int]:
        ans=[]
        heap=[]
        n=len(arr)
        for i in range(k):
            heapq.heappush(heap,[-arr[i],i])
        ans.append(-heap[0][0])
        for i in range(k,n):
            heapq.heappush(heap,[-arr[i],i])
            while heap[0][1]<=i-k:
                heapq.heappop(heap)
        
            ans.append(-heap[0][0])
        return ans
        
        
        
        
        
        
        
        
        
        
        

        