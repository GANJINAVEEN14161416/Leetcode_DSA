#User function Template for python3
from collections import *
from math import *
from sys import *
from os import *
class Solution:
	def singleNumber(self, nums):
        list1=[]
        xor=0
        for i in range(len(nums)):
            xor=xor^nums[i]
        x=y=0
        right=xor & (-xor)
        for i in range(len(nums)):
            if (right & nums[i]):
                x=x^nums[i]
            else:
                y=y^nums[i]
        list1.append(x)
        list1.append(y)
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