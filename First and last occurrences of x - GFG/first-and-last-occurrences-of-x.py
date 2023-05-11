#User function Template for python3


def find(arr,n,x):
    list1=[]
    if x not in arr:
        return [-1,-1]
    list1.append(arr.index(x))
    for i in range(len(arr)-1,-1,-1):
        if arr[i]==x:
            list1.append(i)
            break
    return list1
    



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