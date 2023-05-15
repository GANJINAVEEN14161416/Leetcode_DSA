#User function Template for python3

class Solution:

    def lookandsay(self, n):
        look="1"
        for i in range(n-1):
            say=""
            count=1
            current=look[0]
            for k in look[1:]:
                if k==current:
                    count+=1
                else:
                    say+=str(count)+current
                    count=1
                    current=k
            say+=str(count)+current
            look=say
        return  look
                    
            


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