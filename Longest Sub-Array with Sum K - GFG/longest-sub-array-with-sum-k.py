#User function Template for python3
from collections import *
class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        dic={}
        prefix,ans=0,0
        dic[0]=-1
        for i in range(len(arr)):
            prefix+=arr[i]
            if (prefix-k) in dic.keys():
                ans=max(ans,i-dic[prefix-k])
            if prefix not in dic:
                dic[prefix]=i   
        return ans

    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n, k = map(int , input().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.lenOfLongSubarr(arr, n, k))




# } Driver Code Ends