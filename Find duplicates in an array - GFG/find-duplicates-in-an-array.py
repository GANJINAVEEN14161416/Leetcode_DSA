class Solution:
    def duplicates(self, arr, n): 
        from collections import Counter
        return sorted([key for key, value in Counter(arr).items() if value > 1]) or [-1]

#{ 
 # Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends