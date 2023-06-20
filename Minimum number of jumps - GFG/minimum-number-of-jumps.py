#User function Template for python3
class Solution:
    def minJumps(self, arr, n):
        count=end=start=0
        for i in range(len(arr)-1):
            start=max(start,i+arr[i])
            if end==i:
                end=start
                count+=1
            if arr[i]==0 and end==i:
                return -1
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        Arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minJumps(Arr,n)
        print(ans)
# } Driver Code Ends