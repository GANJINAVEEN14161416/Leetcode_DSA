#User function Template for python3


def find(arr,n,x):
    if x not in arr:
        return [-1,-1]
    a=arr.index(x)
    for i in range(n-1,-1,-1):
        if arr[i]==x:
            b=i
            return [a,b]
            break
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