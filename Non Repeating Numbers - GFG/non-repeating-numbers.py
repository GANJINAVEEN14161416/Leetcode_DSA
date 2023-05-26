#User function Template for python3

class Solution:
	def singleNumber(self, nums):
	    from collections import Counter
	    dic=Counter(nums)
	    list1=[]
	    for i,c in dic.items():
	        if c==1:
	            list1.append(i)
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