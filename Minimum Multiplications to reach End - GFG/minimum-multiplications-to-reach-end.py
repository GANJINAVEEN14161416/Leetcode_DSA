#User function Template for python3
from collections import *
from typing import List
 
class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        # code here
        distance=[float('inf')]*100000
        q=deque()
        q.append([0,start])
        mod=10**5
        while q:
            steps,dis=q.popleft()
            if dis==end:
                return steps
            for i in arr:
                val=(i*dis)%mod
                if val<distance[val]:
                    distance[val]=val
                    q.append([steps+1,val])
        return -1
                    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        start, end = list(map(int,input().split()))
        obj=Solution()
        print(obj.minimumMultiplications(arr, start, end))
# } Driver Code Ends