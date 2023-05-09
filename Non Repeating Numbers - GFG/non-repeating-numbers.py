#User function Template for python3
from collections import *
from math import *
from sys import *
from os import *
class Solution:
	def singleNumber(self, nums):
	    list1=[]
	    dic=Counter(nums)
	    for key,value in dic.items():
	        if value==1:
	            list1.append(key)
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