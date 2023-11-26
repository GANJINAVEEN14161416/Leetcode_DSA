
def getFloorAndCeil(arr, n, x):
    arr.sort()
    ans=[]
    fl,cl=-1,-1
    left,right=0,n-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]<=x:
            fl=arr[mid]
            left=mid+1
        if arr[mid]>=x:
            cl=arr[mid]
            right=mid-1
    return [fl,cl]





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