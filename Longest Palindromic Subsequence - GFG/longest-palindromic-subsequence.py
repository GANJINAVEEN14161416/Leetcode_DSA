#User function Template for python3

class Solution:

    def longestPalinSubseq(self, S):
        # code here
        s1=S
        s2=S[::-1]
        x,y=len(s1),len(s2)
        t=[[0]*(y+1) for _ in range(x+1)]
        for i in range(1,x+1):
            for j in range(1,y+1):
                if s1[i-1]==s2[j-1]:
                    t[i][j]=1+t[i-1][j-1]
                else:
                    t[i][j]=max(t[i-1][j],t[i][j-1])
        return t[-1][-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        ob = Solution()
        ans = ob.longestPalinSubseq(s)
        print(ans)
# } Driver Code Ends