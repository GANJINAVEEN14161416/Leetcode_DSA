#User function Template for python3

def rotate(matrix): 
    #code here
    t=0
    l=0
    r=len(matrix)-1
    b=len(matrix)-1
    while l<=r and t<=b:
        for i in range(r-l):
            temp=matrix[t][l+i]
            matrix[t][l+i]=matrix[t+i][r]
            matrix[t+i][r]=matrix[b][r-i]
            matrix[b][r-i]=matrix[b-i][l]
            matrix[b-i][l]=temp
        l+=1
        r-=1
        b-=1
        t+=1


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