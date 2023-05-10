#User function Template for python3
class Solution:
    def setBits(self, N):
        count=0
        while N:
            if N%2:
                count+=1
            N=N//2
        return count
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        ob = Solution()
        ans = ob.setBits(N)
        print(ans)




# } Driver Code Ends