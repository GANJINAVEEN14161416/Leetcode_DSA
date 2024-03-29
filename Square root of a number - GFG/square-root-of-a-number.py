#User function Template for python3


#Complete this function
class Solution:
    def floorSqrt(self, x): 
    #Your code here
        left=0
        right=x
        while left<=right:
            mid=(left+right)//2
            if mid*mid<=x:
                left=mid+1
            else:
                right=mid-1
        return right

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            x=int(input())
            
            print(Solution().floorSqrt(x))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends