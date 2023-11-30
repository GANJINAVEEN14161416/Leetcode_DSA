#User function Template for python3




def getFloorAndCeil(arr, n, x):
    # code here
    arr.sort()
    left=0
    right=n-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==x:
            return [arr[mid],arr[mid]]
        if arr[mid]<x:
            left=mid+1
        else:
            right=mid-1
    if left>=n:
        return [arr[right],-1]
    if right<0:
        return [-1,arr[left]]
    return [arr[right],arr[left]]


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))

        ans = getFloorAndCeil(arr, n, x)
        print(str(ans[0]) + " " + str(ans[1]))
        tc -= 1

# } Driver Code Ends