#User function Template for python3

class Solution:
    def findMaxLen(ob, s):
        open,close,ans=0,0,0
        for i in s:
            if i=="(":
                open+=1
            else:
                close+=1
            if close==open:
                ans=max(ans,close+open)
            elif close>open:
                open=close=0
        open=close=0
        for i in range(len(s)-1,-1,-1):
            if "("==s[i]:
                open+=1
            else:
                close+=1
            if close==open:
                ans=max(ans,close+open)
            elif open>close:
                open=close=0
        return ans
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S=input()
        
        ob = Solution()
        print(ob.findMaxLen(S))
# } Driver Code Ends