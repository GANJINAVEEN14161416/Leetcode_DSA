#User function Template for python3

class Solution:

    def lookandsay(self, n):
        first="1"
        for i in range(n-1):
            new=""
            count=1
            current=first[0]
            for c in first[1:]:
                if c==current:
                    count+=1
                else:
                    new+=str(count)+current
                    current=c
                    count=1
            new+=str(count)+current
            first=new
        return first


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        n = int(input())

        solObj = Solution()

        print(solObj.lookandsay(n))

# } Driver Code Ends