#Back-end complete function Template for Python 3

class Solution:
    def maxSubStr(self,str):
        c1,c2=0,0
        count=0
        n=len(str)
        for i,s in enumerate(str):
            if s=="0":
                c1+=1
            if s=="1":
                c2+=1
            if c1==c2:
                count+=1
        if c1!=c2:
            return -1
        return count



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        s=input()
        obj=Solution()
        ans=obj.maxSubStr(s)
        print(ans)
# } Driver Code Ends