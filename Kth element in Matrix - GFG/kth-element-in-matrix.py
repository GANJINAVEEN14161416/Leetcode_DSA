#User function Template for python3

def kthSmallest(mat, n, k): 
    # Your code goes here
    left,right=mat[0][0],mat[-1][-1]
    while left<=right:
        mid=(left+right)//2
        count=0
        for row in mat:
            count+=counter(row,mid)
        if count<k:
            left=mid+1
        else:
            right=mid-1
    return left
    
    
    
def counter(row,mid):
    i=0
    count=0
    while i<len(row) and row[i]<=mid:
        count+=1
        i+=1
    return count
    
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Driver Code 

def main():
    T=int(input())
    while(T>0):
        n = int(input())
        mat=[[0 for j in range(n)] for i in range(n)]
        line1=[int(x) for x in input().strip().split()]
        k = int(input())

        temp=0
        for i in range(n):
            for j in range (n):
                mat[i][j]=line1[temp]
                temp+=1
        
        print(kthSmallest(mat, n, k))
        T-=1


if __name__=="__main__":
    main()




# } Driver Code Ends