#User function Template for python3

class Solution:
    def wordBreak(self, n, wordDict, s):
        # code here
        dic={}
        def wordbreak1(s):
            if s not in dic:
                ans=[]
                for w in wordDict:
                    if s[:len(w)]==w:
                        if len(s)==len(w):
                            ans.append(w)
                        else:
                            for word in wordbreak1(s[len(w):]):
                                ans.append(w+" "+word)
                dic[s]=ans
            return dic[s]
        return wordbreak1(s)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        dicti = input().split()
        s = input()
        
        ob = Solution()
        ans = ob.wordBreak(n, dicti, s)
        if(len(ans) == 0):
            print("Empty")
        else:
            ans.sort()
            for it in (ans):
                print("("+it,end = ")")
            print()
# } Driver Code Ends