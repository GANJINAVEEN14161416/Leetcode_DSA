#User function Template for python3

class Solution:
    def longestCommonPrefix(self, arr, n):
        arr.sort()
        less=arr[0]
        ans=""
        for i in range(len(less)):
            if less[i]==arr[n-1][i]:
                ans+=less[i]
            else:
                break
        return ans if len(ans)>0 else "-1"
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        arr = [x for x in input().strip().split(" ")]
        
        ob=Solution()
        print(ob.longestCommonPrefix(arr, n))
# } Driver Code Ends