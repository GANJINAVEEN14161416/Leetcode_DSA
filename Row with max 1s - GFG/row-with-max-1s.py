#User function Template for python3
class Solution:

	def rowWithMax1s(self,arr, n, m):
		maxindex=-1
		temp=0
		count=0
		for i in range(n*m):
		    if arr[i//m][i%m]==1:
		        count+=1
		    if count>temp:
		        temp=count
		        maxindex=i//m
		    if i%m==m-1:
		        count=0
	    return maxindex
		      
		        
		
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))
        
        inputLine = list(map(int, input().strip().split()))
        arr = [[0 for j in range(m)] for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                arr[i][j] = inputLine[i * m + j]
        ob = Solution()
        ans = ob.rowWithMax1s(arr, n, m)
        print(ans)
        tc -= 1

# } Driver Code Ends