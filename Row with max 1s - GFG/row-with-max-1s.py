#User function Template for python3
from collections import *
class Solution:

	def rowWithMax1s(self,arr, n, m):
		dic=defaultdict(list)
		for i in range(len(arr)):
		    dic[i]=arr[i].count(1)
		count=0
		value=0
		for i,v in dic.items():
		    if v>value:
		        value=v
		        count=i
		if value==0:
		    return -1
		return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))
        
        inputLine = list(map(int, input().strip().split()))
        arr = [[0 for j in range(m)] for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                arr[i][j] = inputLine[i * m + j]
        ob = Solution()
        ans = ob.rowWithMax1s(arr, n, m)
        print(ans)
        tc -= 1

# } Driver Code Ends