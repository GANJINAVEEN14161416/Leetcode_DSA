from collections import *
class Solution:

    #Function to find distance of nearest 1 in the grid for each cell.
	def nearest(self, mat):
		#Code here
        row=len(mat)
        col=len(mat[0])
        q=deque()
        steps=0
        visit=[[False]*col for i in range(row)]
        for i in range(row):
            for j in range(col):
                if mat[i][j]==1:
                    visit[i][j]=True
                    q.append([i,j,steps])
        m1=[0,-1,0,1]
        m2=[1,0,-1,0]
        while q:
            r,c,steps=q.popleft()
            mat[r][c]=steps
            for new in range(4):
                newrow=r+m1[new]
                newcol=c+m2[new]
                if newrow>=0 and newrow<row and newcol>=0 and newcol<col and not visit[newrow][newcol]:
                    visit[newrow][newcol]=True
                    q.append([newrow,newcol,steps+1])     
        return mat


#{ 
 # Driver Code Starts

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = map(int, input().split())
		grid = []
		for _ in range(n):
			a = list(map(int, input().split()))
			grid.append(a)
		obj = Solution()
		ans = obj.nearest(grid)
		for i in ans:
			for j in i:
				print(j, end = " ")
			print()

# } Driver Code Ends