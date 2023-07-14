#User function Template for python3

class Solution:
    def allPalindromicPerms(self, S):
        n=len(S)
        ans=[]
        def solve(start,path):
            if start==n:
                ans.append(path)
                return 
            for i in range(start,n):
                if S[start:i+1]==S[start:i+1][::-1]:
                    solve(i+1,path+[S[start:i+1]])
        solve(0,[])
        return ans
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S=input()
        
        ob = Solution()
        allPart = ob.allPalindromicPerms(S)
        for i in range(len(allPart)): 
            for j in range(len(allPart[i])): 
                print(allPart[i][j], end = " ") 
            print() 
# } Driver Code Ends