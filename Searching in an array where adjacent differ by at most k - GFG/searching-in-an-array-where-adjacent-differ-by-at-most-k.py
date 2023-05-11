#User function Template for python3

def search (arr, n, x, k) : 
    i = 0
    while (i < n):
     
        # If x is found at index i
        if (arr[i] == x):
            return i
 
        # Jump the difference between current
        # array element and x divided by k
        # We use max here to make sure that i
        # moves at-least one step ahead.
        i = i + max(1, int(abs(arr[i] - x) / k))
    return -1



#{ 
 # Driver Code Starts
#Initial Template for Python 3

    

for _ in range(0,int(input())):
    n, k = map(int , input().split())
    arr = list(map(int, input().strip().split()))
    x = int(input())
    ans = search(arr, n, x, k)
    print(ans)




# } Driver Code Ends