#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
from collections import *
class Solution:
    def characterReplacement(self, s, k):
        # Code here
        left=maxf=0
        dic=defaultdict(int)
        for right in range(len(s)):
            dic[s[right]]+=1
            maxf=max(maxf,dic[s[right]])
            if (right-left+1)>maxf+k:
                dic[s[left]]-=1
                left+=1
        return len(s)-left

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range(t):
        S = input().strip()
        K = int(input())
        ob = Solution()
        res = ob.characterReplacement(S, K)
        print(res)
# } Driver Code Ends