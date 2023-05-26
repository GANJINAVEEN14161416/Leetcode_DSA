#User function Template for python3
from collections import *
from sys import *
from os import *
from math import *
from itertools import combinations
class Solution:
	def AllPossibleStrings(self, s):
		# Code here
		list1=[]
		list2=[]
		for i in s:
		    list1.append(i)
	    for i in range(1,len(s)+1):
	        for j in combinations(s,i):
	            list2.append("".join(j))
	    return sorted(list2)
	            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution();
		ans = ob.AllPossibleStrings(s)
		for i in ans:
			print(i, end = " ");
		print()
# } Driver Code Ends