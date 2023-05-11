#User function template for Python 3
from collections import *
class Solution:
    def majorityElement(self, A, N):
        dic=Counter(A)
        maj=0
        num=0
        for key,val in dic.items():
            if val>maj:
                maj=val
                num=key
        if maj>N/2:
            return num
        return -1
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends