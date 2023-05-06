#User function Template for python3

class Solution:
    def median(self, matrix, R, C):
        list1=[]
    	for r in range(len(matrix)):
    	    for c in range(len(matrix[0])):
    	        list1.append(matrix[r][c])
    	n=len(list1)
    	list1.sort()
    	if n%2==0:
    	    return (list1[n//2]+list1[n//2+1])/2
        return list1[n//2]
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        r,c = map(int,input().strip().split())
        matrix = [[0 for j in range(c)] for i in range(r)]
        for i in range(r):
            t=[int(el) for el in input().split()]
            for j in range(c):
                matrix[i][j]=t[j]
        ans = ob.median(matrix, r, c);
        print(ans)
# } Driver Code Ends