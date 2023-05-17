#User function Template for python3

class Solution:
    
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        one,two=[0]*n,[0]*n
        for i in range(n):
            for j in range(n):
                if M[i][j]==1:
                    one[j]+=1
                    two[i]+=1
        for i in range(n):
            if one[i]==(n-1) and two[i]==0:
                return i
        return -1

        # for i in range(n):

        #     f=0

        #     for j in range(n):

        #         if(M[i][j]!=0):

        #             f=1

        #             break

        #     if f!=1:

        #         arr.append(i)

                

        # for i in arr:

        #     f=0

        #     for j in range(n):

        #         if(M[j][i]!=1 and i!=j):

        #             f=1

        #             break

        #     if f==0:

        #         return i

        # return -1



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        k = 0
        m = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(a[k])
                k+=1
            m.append(row)
        ob = Solution()
        print(ob.celebrity(m,n))
# } Driver Code Ends