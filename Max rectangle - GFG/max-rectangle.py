#User function Template for python3


class Solution:
    def maxArea(self,M, n, m):
        height=[0]*(m)
        maxarea=0
        for r in range(n):
            for c in range(m):
                if M[r][c]==1:
                    height[c]+=1
                else:
                    height[c]=0
            stack=[]
            for i,h in enumerate(height):
                start=i
                while stack and h<stack[-1][1]:
                    index,hi=stack.pop()
                    start=index
                    maxarea=max(maxarea,(i-index)*hi)
                stack.append([start,h])
            for i,h in stack:
                maxarea=max(maxarea,(len(height)-i)*h)
        return maxarea

#{ 
 # Driver Code Starts
#Initial Template for Python 3



# Driver Code 
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        R,C = map(int, input().strip().split())
        A = []
        for i in range(R):
            line = [int(x) for x in input().strip().split()]
            A.append(line)
        print(Solution().maxArea(A, R, C)) 
	
# This code is contributed 
# by SHUBHAMSINGH10 

# } Driver Code Ends