#User function Template for python3

def rotate(matrix): 
    #code here
    t=0
    l=0
    r=len(matrix)-1
    b=len(matrix)-1
    list2=[]
    while l<=r:
        list1=[]
        for i in range(t,b+1):
            list1.append(matrix[i][r])
        list2.append(list1)
        r-=1
    matrix[::]=list2[::]
    #return list2
        


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