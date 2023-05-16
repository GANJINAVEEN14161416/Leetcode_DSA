#User function Template for python3


class Solution:
    def minFlips(self, s):
        n=len(s)
        count=0
        count2=0
        for i in range(n):
            if i%2==0:
                if s[i]!="1":
                    count+=1
            elif s[i]!="0":
                count+=1
        return min(count,len(s)-count)
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        S=input()
        Obj=Solution()
        ans=Obj.minFlips(S)
        print(ans)
# } Driver Code Ends