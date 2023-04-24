class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        list1=[-x for x in stones]
        while len(list1)>1:
            heapq.heapify(list1)
            a,b=heapq.heappop(list1),heapq.heappop(list1)
            heapq.heappush(list1,-(abs(a-b)))
        return abs(list1[0])
        
            
        