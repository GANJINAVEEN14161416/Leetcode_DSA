#User function Template for python3
from collections import *
class Solution:
    def findTwoElement( self,arr, n):
        A=set(range(1,n+1))
        B=set(arr)
        missing=list(A-B)[0]
        dic=Counter(arr)
        twice=0
        for key,val in dic.items():
            if val==2:
                twice=key
                break
        return [twice,missing]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends