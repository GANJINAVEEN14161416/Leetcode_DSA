#User function Template for python3

def Search(arr,n,k):
    left=0
    right=n-1
    if k not in arr:
        return -1
    while left<right:
        if arr[left]==k:
            return left
        if arr[right]==k:
            return right
        left+=1
        right-=1


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