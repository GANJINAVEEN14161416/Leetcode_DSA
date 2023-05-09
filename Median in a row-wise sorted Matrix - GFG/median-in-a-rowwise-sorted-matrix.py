#User function Template for python3

class Solution:
    def median(self, matrix, R, C):
    	list1 = []
    	for i in range(len(matrix)):
    	    for j in range(len(matrix[0])):
    	        list1.append(matrix[i][j])
    	list1.sort()
    	return list1[len(list1)//2]
    	        
    	        

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