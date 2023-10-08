#User function Template for python3

class Solution:
    def minPartition(self, N):
        # code here
        listofCoins=[1,2,5,10,20,50,100,200,500,2000]
        ans=[]
        while(N):
            for i in range(len(listofCoins)-1,-1,-1):
                if listofCoins[i]<=N:
                    ans.append(listofCoins[i])
                    N-=listofCoins[i]
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