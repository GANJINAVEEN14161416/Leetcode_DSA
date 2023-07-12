from collections import *
class Solution:

	#Function to find out minimum steps Knight needs to reach target position.
	def minStepToReachTarget(self, KnightPos, TargetPos, N):
	    q=deque()
		m1=[[-2,1],[-2,-1],[-1,-2],[1,-2],[2,-1],[2,1],[1,2],[-1,2]]
		k1,k2=KnightPos[0],KnightPos[1]
		q.append([k1-1,k2-1,0])
		visit=[[False]*N for i in range(N)]
		visit[k1-1][k2-1]=True
		t1,t2=TargetPos[0]-1,TargetPos[1]-1
		while q:
		    r,c,steps=q.popleft()
		    if t1==r and t2==c:
		        return steps
		    for l1,l2 in m1:
		        row=r+l1
		        col=c+l2
		        if row>=0 and row<N and col>=0 and col<N and not visit[row][col]:
		            q.append([row,col,steps+1])
		            visit[row][col]=True
	    return -1
		            
		    


#{ 
 # Driver Code Starts

T=int(input())
for i in range(T):
	N = int(input())
	KnightPos = list(map(int, input().split()))
	TargetPos = list(map(int, input().split()))
	obj = Solution()
	ans = obj.minStepToReachTarget(KnightPos, TargetPos, N)
	print(ans)

# } Driver Code Ends