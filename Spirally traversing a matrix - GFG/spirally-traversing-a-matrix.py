#User function Template for python3

class Solution:
    
    #Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self,matrix, r, c): 
        # code here 
        list1=[]
        l=0
        r=len(matrix[0])-1
        t=0
        b=len(matrix)-1
        while l<=r and t<=b:
            for i in range(l,r+1):
                list1.append(matrix[t][i])
            t+=1
            for i in range(t,b+1):
                list1.append(matrix[i][r])
            r-=1
            if len(matrix)*len(matrix[0])!=len(list1):
                for i in range(r,l-1,-1):
                    list1.append(matrix[b][i])
                b-=1
                for i in range(b,t-1,-1):
                    list1.append(matrix[i][l])
                l+=1
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