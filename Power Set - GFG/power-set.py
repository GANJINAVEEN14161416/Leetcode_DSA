#User function Template for python3

class Solution:
	def AllPossibleStrings(self, s):
		# Code here
		n=len(s)
		list1=[]
		for i in range(1,2**n):
		    word=""
		    j=0
		    while i>0:
		        if i&1:
		            word+=s[j]
		        i=i>>1
		        j+=1
	        list1.append(word)
	    return sorted(list1)


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