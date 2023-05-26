#User function Template for python3

class Solution:
    def sortedMatrix(self,N,Mat):
        m=[[0]*N for i in range(N)]
        list1=[]
        for i in range(N):
            list1+=Mat[i]
        list1.sort()
        p=0
        for i in range(N):
            for j in range(N):
                m[i][j]=list1[p]
                p+=1
        return m


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