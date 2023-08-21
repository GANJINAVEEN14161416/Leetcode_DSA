#User function Template for python3
from collections import *
class Solution:
    def search(self, A, N):
        # your code here
        dic=defaultdict(int)
        for right in A:
            dic[right]+=1
        for key,value in dic.items():
            if value==1:
                return key
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		n = int (input ())
		arr = list(map(int, input().split()))
		ob = Solution()
		print(ob.search(arr, n)) 
# } Driver Code Ends