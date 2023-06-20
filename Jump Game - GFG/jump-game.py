#User function Template for python3

class Solution:
    def canReach(self, A, N):
        goal=N-1
        for i in range(N-1,-1,-1):
            if i+A[i]>=goal:
                goal=i
        return 1 if goal==0 else 0
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        A=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.canReach(A,N))
# } Driver Code Ends