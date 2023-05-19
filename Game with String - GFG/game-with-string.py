#User function Template for python3
import heapq
import collections
class Solution:
    def minValue(self, s, k):
        dic=collections.Counter(s)
        heap=[[-count,c] for c,count in dic.items()]
        heapq.heapify(heap)
        while k>0:
            count,c=heapq.heappop(heap)
            if count<0:
                count+=1
                heapq.heappush(heap,[count,c])
                k-=1
        value=0
        for i,v in heap:
            value+=(i*i)
        return value


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        k = int(input())
        
        ob = Solution()
        print(ob.minValue(s, k))
# } Driver Code Ends