from collections import *
class Solution:
    def checkMirrorTree(self, n, e, A, B):
        dic=defaultdict(list)
        for i in range(0,2*e,2):
            if A[i] not in dic:
                dic[A[i]].append(A[i+1])
            else:
                dic[A[i]].append(A[i+1])
        for i in range(0,2*e,2):
            if B[i] not in dic:
                return 0
            else:
                if B[i+1]!=dic[B[i]].pop():
                    return 0
        return 1



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n,e=map(int,input().split())
        
        A=list(map(int,input().split()))
        B=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.checkMirrorTree(n,e,A,B))
# } Driver Code Ends