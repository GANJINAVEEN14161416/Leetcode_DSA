#User function Template for python3

class Solution:
    def findMaxLen(ob, S):
        stack=[]
        ans=0
        stack.append(-1)
        for i in range(len(S)):
            if S[i]=='(':
                stack.append(i)
            else:
                stack.pop()
                if stack==[]:
                    stack.append(i)
                ans=max(ans,i-stack[-1])
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