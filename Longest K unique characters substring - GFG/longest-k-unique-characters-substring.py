#User function Template for python3
from collections import *

class Solution:

    def longestKSubstr(self, s, k):
        # code here
        j=0
        dic=defaultdict(int)
        n=len(s)
        i=0
        mx=0
        while j<n:
            dic[s[j]]+=1
            if len(dic)<k:
                j+=1
            elif len(dic)==k:
                mx=max(mx,j-i+1)
                j+=1
            elif len(dic)>k:
                while len(dic)>k:
                    dic[s[i]]-=1
                    if dic[s[i]]==0:
                        del dic[s[i]]
                    i+=1
                j+=1
        return mx if mx else -1



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()
        k = int(input())

        solObj = Solution()

        ans = solObj.longestKSubstr(s, k)

        print(ans)

# } Driver Code Ends