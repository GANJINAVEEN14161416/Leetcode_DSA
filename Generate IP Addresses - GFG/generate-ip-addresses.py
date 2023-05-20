#Your Function should return a list containing all possible IP address
#No need to worry about order
class Solution:
    def genIp(self, s):
        ans = []
        k = 0

        def backtrack(s, ans,k, temp=''):
            if k==4 and len(s)==0:
                ans.append(temp[:-1])
                return
            if k==4 or len(s)==0:
                return
            
            for i in range(3):
                if k>4 or i+1>len(s):
                    break
                
                if int(s[:i+1])>255:
                    continue
                if i != 0 and s[0]=='0':
                    continue
                        
                backtrack(s[i+1:], ans, k+1, temp+s[:i+1]+'.')
        backtrack(s,ans,k,'')
        return ans


#{ 
 # Driver Code Starts
#Main
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s = input().strip()
        res = Solution().genIp(s)
        res.sort()
        if(len(res)):
            for u in res:
                print(u)
        else:
            print(-1)
# } Driver Code Ends