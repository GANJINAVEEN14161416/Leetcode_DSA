#User function Template for python3
from collections import *
import heapq
class Solution:
    def minValue(self, s, k):
        # code here
        c=Counter(s)
        heap=[[-freq,ch] for ch,freq in c.items()]
        heapq.heapify(heap)
        ans=0
        while heap and k:
            freq,ch=heapq.heappop(heap)
            freq+=1
            k-=1
            heapq.heappush(heap,[freq,ch])
        for f,i in heap:
            ans+=f**2
        return ans

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