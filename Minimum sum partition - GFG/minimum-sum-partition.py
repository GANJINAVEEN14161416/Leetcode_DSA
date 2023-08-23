#User function Template for python3
class Solution:
    def minDifference(self, arr, n):
        x=sum(arr)
        def subset(arr,summ):
            prev=[False]*(summ+1)
            prev[0]=True
            N=len(arr)
            for ind in range(1,N+1):
                cur=[False]*(summ+1)
                cur[0]=True
                for target in range(1,summ+1):
                    nottake=prev[target]
                    take=False
                    if arr[ind-1]<=target:
                        take=prev[target-arr[ind-1]]
                    cur[target]=take or nottake
                prev=cur
            ans=float('inf')
            for i in range(summ+1):
                if prev[i]==True:
                    s1=i
                    s2=summ-i
                    ans=min(ans,abs(s1-s2))
            return ans
        return subset(arr,x)
        
        




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minDifference(arr, N)
		print(ans)

# } Driver Code Ends