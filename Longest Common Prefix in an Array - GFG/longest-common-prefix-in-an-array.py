#User function Template for python3

class Solution:
    def longestCommonPrefix(self, strs, n):
        s=""
        for i in range(len(strs[0])):
            less=strs[0][i]
            for word in strs:
                if i==len(word) or word[i]!=less[i:
                    if len(s)==0:
                        return -1
                    return s
            s=s+less  
        return s
        
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        arr = [x for x in input().strip().split(" ")]
        
        ob=Solution()
        print(ob.longestCommonPrefix(arr, n))
# } Driver Code Ends