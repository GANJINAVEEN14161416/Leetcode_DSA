def push(arr, ele):
    arr.append(ele)
def pop(arr):
    if len(arr)>0:
        arr.pop()
    else:
        return -1
def isFull(n, arr):
    if len(arr)>=n:
        return True
    else:
        return  False
def isEmpty(arr):
    if arr==[]:
        return True
    else:
        return False
def getMin(n, arr):
    return min(arr)


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        stack = []
        while(not isEmpty(stack)):
            pop(stack)
            
        for i in range(n):
            push(stack, arr[i])
        print(getMin(n, stack))
# contributed by: Harshit Sidhwa

# } Driver Code Ends