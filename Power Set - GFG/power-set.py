#User function Template for python3

class Solution:
	def AllPossibleStrings(self, s):
		ans=[]
	    n=len(s)
		for i in range(1,2**n):
		    s1=""
		    for j in range(n):
		        if (i&1<<j):
		            s1+=s[j]
		    ans.append(s1)
	    return sorted(ans)
		    


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