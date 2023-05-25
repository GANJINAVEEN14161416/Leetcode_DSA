#User function Template for python3

class Solution:
    def search(self, patt, s):
        n,res=len(patt),[]
        for i in range(len(s)):
            if s[i:i+n]==patt:
                res.append(i+1)
        return res if len(res) else [-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        for value in ans:
            print(value,end = ' ')
        print()
# } Driver Code Ends