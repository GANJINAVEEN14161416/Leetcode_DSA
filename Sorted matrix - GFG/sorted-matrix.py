#User function Template for python3

class Solution:
    def sortedMatrix(self,N,Mat):
        list1 = []
        for r in range(len(Mat)):
            for c in range(len(Mat)):
                list1.append(Mat[r][c])
        list1.sort()
        matrix=[[0 for i in range(N)] for j in range(N)]
        i=0
        for r in range(len(Mat)):
            for c in range(len(Mat)):
                matrix[r][c] = list1[i]
                i+=1
        return matrix
                
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        v=[]
        for i in range(N):
            a=list(map(int,input().strip().split()))
            v.append(a)
        ob=Solution()
        ans=ob.sortedMatrix(N,v)
        for i in range(N):
            for j in range(N):
                print(ans[i][j],end=" ")
            print()
# } Driver Code Ends