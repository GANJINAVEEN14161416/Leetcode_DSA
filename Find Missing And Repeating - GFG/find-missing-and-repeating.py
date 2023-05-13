#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n): 
        A=set(range(1,n+1))
        missing=list(A-set(arr))[0]
        dic={}
        for i in arr:
            if i not in dic:
                dic[i]=0
            dic[i]+=1
            if dic[i]==2:
                twice=i
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