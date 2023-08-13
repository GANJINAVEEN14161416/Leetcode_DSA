class Solution:
    def minAbsoluteDifference(self, nums: List[int], k: int) -> int:
        if not k:  return 0
        
        nums=sorted((val,idx) for idx,val in enumerate(nums)) 

        stack1, stack2, res =[], [], float('inf')  

        for val,idx in nums:

            while stack1 and stack1[0][0]<=idx:                
                 res=min(res, val-heapq.heappop(stack1)[1])  

            while stack2 and -stack2[0][0]>=idx:                
                res=min(res, val-heapq.heappop(stack2)[1]) 

            heapq.heappush(stack1,(idx+k,val)) 
            heapq.heappush(stack2,(-idx+k,val))   

        return res