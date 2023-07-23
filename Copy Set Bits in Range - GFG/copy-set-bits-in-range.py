#User function Template for python3

class Solution:
    def setSetBit(self, x, y, l, r):
        # code here
        if (l < 1 or r > 32):
            return x;
 
    # Traverse in given range
        for i in range(l, r + 1):
           
            # Find a mask (A number whose
            # only set bit is at i'th position)
            mask = 1 << (i - 1);
     
            # If i'th bit is set in y, set i'th
            # bit in x also.
            if ((y & mask) != 0):
                x = x | mask;
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