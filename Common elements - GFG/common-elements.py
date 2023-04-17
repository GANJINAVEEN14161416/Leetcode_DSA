#User function Template for python3

class Solution:
    def commonElements (self,A, B, C, n1, n2, n3):
        list1=[]
        m1,m2,m3=set(A),set(B),set(C)
        for i in m1:
            if i in m2 and i in m3:
                if i not in list1:
                    list1.append(i)
        return sorted(list1)


#{ 
 # Driver Code Starts
#Initial Template for Python 3


t = int (input ())
for tc in range (t):
    n1, n2, n3 = list(map(int,input().split()))
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(map(int,input().split()))
    
    ob = Solution()
    
    res = ob.commonElements (A, B, C, n1, n2, n3)
    
    if len (res) == 0:
        print (-1)
    else:
        for i in range (len (res)):
            print (res[i], end=" ")
        print ()

# } Driver Code Ends