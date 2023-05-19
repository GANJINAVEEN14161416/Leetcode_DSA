#User function Template for python3

def printFirstNegativeInteger( A, N, K):
    q,l,h,res = [],0,K-1,[]
    for i in range(K):
        if A[i] < 0:
            q.append(A[i])
    while (h < N):
        if q: res.append(q[0])
        else: res.append(0)
        if A[l] < 0: q.pop(0)
        l += 1
        if h == N-1: break
        h += 1
        if A[h] < 0: q.append(A[h])
    return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        answer = printFirstNegativeInteger(a, n, k)
        for i in answer:
            print(i,end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends