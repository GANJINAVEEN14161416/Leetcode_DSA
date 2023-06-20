#User function Template for python3

class Solution:
    def getMinDiff(self, arr, n, k):
        arr.sort()
        ans = arr[-1]- arr[0]
        for i in range(1, n):
            if arr[i] - k < 0:
                 continue
            max_ = max(arr[i-1] + k, arr[-1] - k)
            min_ = min(arr[i] - k, arr[0] + k)
            ans = min(ans, max_ - min_)
        return ans
            
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends