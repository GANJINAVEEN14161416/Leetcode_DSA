from collections import *
class Solution:
	def floodFill(self, image, sr, sc, color):
		if image[sr][sc]==color:
            return image
        q=deque()
        q.append([sr,sc])
        temp=image[sr][sc]
        rowmatrix=[0,-1,0,1]
        colmatrix=[1,0,-1,0]
        visit=[[False]*len(image[0]) for i in range(len(image))]
        visit[sr][sc]=True
        image[sr][sc]=color
        while q:
            row,col=q.popleft()
            for i in range(4):
                newrow=row+rowmatrix[i]
                newcol=col+colmatrix[i]
                if newrow>=0 and newrow<len(image) and newcol>=0 and newcol<len(image[0]) and not visit[newrow][newcol] and image[newrow][newcol]==temp:
                    q.append([newrow,newcol])
                    image[newrow][newcol]=color
                    visit[newrow][newcol]=True
        return image



#{ 
 # Driver Code Starts
import sys
sys.setrecursionlimit(10**7)


T=int(input())
for i in range(T):
	n, m = input().split()
	n = int(n)
	m = int(m)
	image = []
	for _ in range(n):
		image.append(list(map(int, input().split())))
	sr, sc, newColor = input().split()
	sr = int(sr); sc = int(sc); newColor = int(newColor);
	obj = Solution()
	ans = obj.floodFill(image, sr, sc, newColor)
	for _ in ans:
		for __ in _:
			print(__, end = " ")
		print()
# } Driver Code Ends