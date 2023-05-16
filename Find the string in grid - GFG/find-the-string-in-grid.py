#User function Template for python3

class Solution:
	def searchWord(self, grid, word):
        n,m,l,x = len(grid),len(grid[0]),len(word),[]
        def helper(i,j,k,n,m,l,di,dj):
            if k == l:
                return True
            if j<0 or i<0 or j>=m or i>=n or grid[i][j]!= word[k]: 
                return False
            return helper(i+di,j+dj,k+1,n,m,l,di,dj)
        moves = [[0,1],[1,0],[0,-1],[-1,0],[1,1],[1,-1],[-1,-1],[-1,1]]
        for i in range(n):
            for j in range(m):
                for di,dj in moves:
                    if grid[i][j] == word[0]:
                        if helper(i,j,0,n,m,l,di,dj):
                            x.append([i,j])
                            break
        return x

#  def helper(i,j,k,n,m,l,di,dj):

#      if k == l:

#          return True

#      if j<0 or i<0 or j>=m or i>=n or grid[i][j] != word[k]:

#          return False

#      return helper(i+di,j+dj,k+1,n,m,l,di,dj)

     

#      moves = [[0,1],[1,0],[0,-1],[-1,0],[1,1],[1,-1],[-1,-1],[-1,1]]

#      for i in range(n):

#          for j in range(m):

#              for di,dj in moves:

#                  if grid[i][j] == word[0]:

#                      if helper(i,j,0,n,m,l,di,dj):

#                          x.append([i,j])

#                          break

#      return x

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n); m = int(m);
		grid = []
		for _ in range(n):
			cur  = input()
			temp = []
			for __ in cur:
				temp.append(__)
			grid.append(temp)
		word = input()
		obj = Solution()
		ans = obj.searchWord(grid, word)
		for _ in ans:
			for __ in _:
				print(__, end = " ")
			print()
		if len(ans)==0:
		    print(-1)

# } Driver Code Ends