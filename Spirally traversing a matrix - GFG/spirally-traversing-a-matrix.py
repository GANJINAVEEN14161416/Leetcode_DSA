#User function Template for python3

class Solution:
    
    #Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self,matrix, r, c):
        left=0
        top=0
        right=c-1
        bottom=r-1
        list1 = []
        while left<=right and top<=bottom:
            for i in range(left,right+1,1):
                list1.append(matrix[top][i])
            top+=1
            for i in range(top,bottom+1,1):
                list1.append(matrix[i][right])
            right-=1
            if left>right or top>bottom:
                break
            for i in range(right,left-1,-1):
                list1.append(matrix[bottom][i])
            bottom-=1
            for i in range(bottom,top-1,-1):
                list1.append(matrix[i][left])
            left+=1
        return list1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(r):
            row=[]
            for j in range(c):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        ans = obj.spirallyTraverse(matrix,r,c)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends