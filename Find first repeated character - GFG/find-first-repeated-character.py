#User function Template for python3

class Solution:
    def firstRepChar(self, s):
        # for i in range(len(s)):
        #     if s[i] in s[:i]:
        #         return s[i]
        # return -1
        from collections import defaultdict
        dic=defaultdict(int)
        for i in s:
            dic[i]+=1
            if dic[i]>1:
                return i
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        print(solObj.firstRepChar(s))
# } Driver Code Ends