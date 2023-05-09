#User function Template for python3
from collections import *
from math import *
from sys import *
from os import *
class Solution:
	def singleNumber(self, nums):
        def UniqueNumbers2(arr, n):
            sums = 0
            for i in range(0, n):
                sums = (sums ^ arr[i])
            sums = (sums & -sums)
            sum1 = 0
            sum2 = 0
            list1=[]
            for i in range(0, len(arr)):
                if (arr[i] & sums) > 0:
                    sum1 = (sum1 ^ arr[i])
                else:
                    sum2 = (sum2 ^ arr[i])
            list1.append(sum1)
            list1.append(sum2)
            return sorted(list1)
        return UniqueNumbers2(nums,len(nums))
        	            



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