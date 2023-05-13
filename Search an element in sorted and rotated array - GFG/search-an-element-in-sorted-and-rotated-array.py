#User function Template for python3

def Search(arr,n,k):
    left,right=0,n-1
    while left<=right:
        mid=(left+right)
        if arr[mid]==k:
            return mid
        elif arr[mid]<k:
            if arr[right]>=arr[mid]:
                right=mid-1
            else:
                left=mid+1
        elif arr[mid]>k:
            if arr[right]>=arr[mid]:
                right=mid-1
            else:
                left=mid+1
    return -1
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tcs=int(input())
    for _ in range(tcs):
        n=int(input())
        arr=[int(x) for x in input().split()]
        k=int(input())

        print(Search(arr,n,k))

# } Driver Code Ends