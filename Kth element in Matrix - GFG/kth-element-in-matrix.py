#User function Template for python3
from collections import *
from sys import *
from os import *
from math import *
import heapq
def kthSmallest(mat, n, k): 
    list1=[]
    for r in range(n):
        for c in range(n):
            heapq.heappush(list1,mat[r][c])
    heapq.heapify(list1)
    for i in range(k-1):
        heapq.heappop(list1)
    return heapq.heappop(list1)




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