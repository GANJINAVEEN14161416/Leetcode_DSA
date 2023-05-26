#User function Template for python3
import bisect
class Solution:
    def median(self, matrix, R, C):
    	mi=min(matrix)[0]
    	mx=max(matrix)[-1]
    	median=(R*C+1)//2
    	while mi<=mx:
    	    mid=(mi+mx)//2
    	    count=0
    	    for r in matrix:
    	        count+=bisect.bisect_right(r,mid)
    	    if count<median:
    	        mi=mid+1
    	    else:
    	        mx=mid-1
        return mi


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