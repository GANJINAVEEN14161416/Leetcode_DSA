#User function Template for python3

class Solution:
	def findMidSum(self, ar1, ar2, n): 
        m=len(ar1)
        n=len(ar2)
        i,j=m-1,0
        while i>=0 and j<n:
            if ar1[i]>ar2[j]:
                ar1[i],ar2[j]=ar2[j],ar1[i]
                i-=1
                j+=1
            else:
                break
        ar1.sort()
        ar2.sort()
        return (ar1[-1]+ar2[0])


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        ar1=list(map(int, input().strip().split()))
        ar2=list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMidSum(ar1, ar2, n)
        print(ans)
        tc=tc-1

# } Driver Code Ends