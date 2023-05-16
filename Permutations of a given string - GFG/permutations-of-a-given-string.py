#User function Template for python3

class Solution:
    def find_permutation(self, s):
        list1=[]
        def dfs(s,temp,list1):
            if len(s)==0:
                if temp not in list1:
                    list1.append(temp)
                return
            for i in range(len(s)):
                dfs(s[:i]+s[i+1:],temp+s[i],list1)
        dfs(s,"",list1)
        return sorted(list1)
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S=input()
		ob = Solution()
		ans = ob.find_permutation(S)
		for i in ans:
			print(i,end=" ")
		print()
# } Driver Code Ends