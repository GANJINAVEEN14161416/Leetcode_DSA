#User function Template for python3


def find(arr,n,x):
    def search(x):
        left,right=0,n-1
        while left<=right:
            mid=(left+right)//2
            if arr[mid]<x:
                left=mid+1
            else:
                right=mid-1
        return left
    a=search(x)
    b=search(x+1)-1
    if a<=b:
        return [a,b]
    return [-1,-1]


#{ 
 # Driver Code Starts
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ans=find(arr,n,x)
    print(*ans)
# } Driver Code Ends