#User function Template for python3

class Solution:
    def longestPalin(self, s):
        def fun(s,l,r):
            n=len(s)
            while l>=0 and r<n and s[l]==s[r]:
                l-=1
                r+=1
            return l+1,r
        start=end=0
        for i in range(len(s)):
            b1,b2=fun(s,i,i)
            if b2-b1>(end-start):
                start=b1
                end=b2
            b1,b2=fun(s,i,i+1)
            if b2-b1>(end-start):
                start=b1
                end=b2
        return s[start:end]
                
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        ob = Solution()

        ans = ob.longestPalin(S)

        print(ans)
# } Driver Code Ends