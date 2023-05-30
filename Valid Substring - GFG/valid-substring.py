#User function Template for python3

class Solution:
    def findMaxLen(ob, S):
        open=close=res=0
        for i in S:
            if i=="(":
                open+=1
            else:
                close+=1
            if close==open:
                res=max(res,close+open)
            elif close>open:
                close=open=0
        open=close=0
        for i in S[::-1]:
            if i=="(":
                open+=1
            else:
                close+=1
            if open==close:
                res=max(res,open+close)
            elif open>close:
                open=close=0
        return res


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