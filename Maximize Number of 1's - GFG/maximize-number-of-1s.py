#User function Template for python3

from collections import *
# m is maximum of number zeroes allowed 
# to flip, n is size of array 
def findZeroes(nums, n, k) :
    res=[0]*2
    ans=left=0
    for right in range(len(nums)):
        res[nums[right]]+=1
        ans=max(ans,res[1])
        if (right-left+1)-res[1]>k:
            res[nums[left]]-=1
            left+=1
    return len(nums)-left

#{ 
 # Driver Code Starts
#Initial Template for Python 3




# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int , input().strip().split()))
        m=int(input())
        ans= findZeroes(arr, n, m)
        print(ans)
        tc=tc-1
# } Driver Code Ends