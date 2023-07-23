#User function Template for python3

class Solution:
    def setSetBit(self, x, y, l, r):
        if l<1 or r>32:
            return x
        for i in range(l,r+1):
            bit=1<<(i-1)
            if (y&bit)!=0:
                x=x|bit
        return x

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        x = int(arr[0])
        y = int(arr[1])
        l = int(arr[2])
        r = int(arr[3])
        
        ob = Solution()
        print(ob.setSetBit(x, y, l, r))
# } Driver Code Ends