class Solution:
	def floodFill(self, image, sr, sc, newColor):
		def dfs(row,col,newColor,sr,sc,sourse,image):
		    if sr<0 or sr>=row or sc<0 or sc>=col:
		        return 
		    if sourse!=image[sr][sc]:
		        return
		    else:
		        image[sr][sc]=newColor
                dfs(row,col,newColor,sr-1,sc,sourse,image)
                dfs(row,col,newColor,sr+1,sc,sourse,image)
                dfs(row,col,newColor,sr,sc-1,sourse,image)
                dfs(row,col,newColor,sr,sc+1,sourse,image)
        if image[sr][sc]==newColor:
            return image
        else:
            dfs(len(image),len(image[0]),newColor,sr,sc,image[sr][sc],image)
            return image
                



#{ 
 # Driver Code Starts
import sys
sys.setrecursionlimit(10**7)
if __name__ == '__main__':

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