#User function Template for python3
from collections import *
class Solution:
	def FirstNonRepeating(self, A):
		# Code here
        visit=[0]*26
        q=deque()
        ans=""
        visited=[0]*26
        for i in A:
            index=ord(i)-97
            if visit[index]==0:
                visit[index]=1
                q.append(i)
            elif visit[index]==1 and i in q:
                q.remove(i)
            if q:
                ans+=q[0]
            else:
                ans+="#"
        return ans
                

#{ 
 # Driver Code Starts

#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		A = input()
		ob = Solution()
		ans = ob.FirstNonRepeating(A)
		print(ans)

# } Driver Code Ends