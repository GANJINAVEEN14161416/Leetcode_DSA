#User function Template for python3

class Solution:
    def minPartition(self, N):
        # code here
        cost=[ 1, 2, 5, 10, 20, 50, 100, 200, 500, 2000 ]
        n=len(cost)
        ans=[]
        for i in range(n-1,-1,-1):
            q=N//cost[i]
            if q>0:
                for k in range(q):
                    ans.append(cost[i])
                N=N%cost[i]
                if N==0:
                    break
        return ans
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        arr = ob.minPartition(N)
        for i in range(len(arr)):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends