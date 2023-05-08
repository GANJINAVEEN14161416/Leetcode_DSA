#User function Template for python3
from collections import *
class Solution:
	def singleNumber(self, nums):
	    dic=Counter(nums)
	    list1=[]
	    for freq,n in dic.items():
	        if n==1:
	            list1.append(freq)
	    return sorted(list1)
	        
		        
		        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		v = list(map(int,input().split()))
		ob = Solution();
		ans = ob.singleNumber(v)
		for i in ans:
			print(i, end = " ")
		print()

# } Driver Code Ends