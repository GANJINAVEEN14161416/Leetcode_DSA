#User function Template for python3

class Solution:
    def findTargetSumWays(self, nums, N, target):
        if target>sum(nums) or (sum(nums)-target)%2==1:
            return 0
        def subset_sum(a, n, sum):
            tab = [[0] * (sum + 1) for i in range(n + 1)]
            tab[0][0] = 1
            for i in range(1, sum + 1):
                tab[0][i] = 0
            for i in range(1, n + 1):
                for j in range(sum + 1):
                    if a[i - 1] <= j:
                        tab[i][j] = tab[i - 1][j] + tab[i - 1][j - a[i - 1]]
                    else:
                        tab[i][j] = tab[i - 1][j]
            return tab[n][sum]
        n=len(nums)
        return subset_sum(nums,n,(sum(nums)-target)//2)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        target = int(input())
        ob = Solution()
        print(ob.findTargetSumWays(arr,N, target))
# } Driver Code Ends