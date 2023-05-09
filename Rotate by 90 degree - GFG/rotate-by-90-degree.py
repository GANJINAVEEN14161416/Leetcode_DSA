#User function Template for python3

def rotate(matrix): 
    left=0
    right=len(matrix)-1
    while left<=right:
        for i in range(right-left):
            top=left
            bottom=right
            temp=matrix[top][left+i]
            matrix[top][left+i]=matrix[top+i][right]
            matrix[top+i][right]=matrix[bottom][right-i]
            matrix[bottom][right-i]=matrix[bottom-i][left]
            matrix[bottom-i][left]=temp
        left+=1
        right-=1
    return matrix
            
#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	t = int(input())
	for _ in range(t):
		N=int(input())
		arr=[int(x) for x in input().split()]
		matrix=[]

		for i in range(0,N*N,N):
			matrix.append(arr[i:i+N])

		rotate(matrix)
		for i in range(N): 
			for j in range(N): 
				print(matrix[i][j], end =' ') 
			print() 
        

# } Driver Code Ends