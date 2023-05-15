#User function Template for python3

class Solution:
    #Function to return sum of count of set bits in the integers from 1 to n.
    def countSetBits(self,n):
        count = 0

    # initialize the factor to 1
        factor = 1
    
        # iterate over each bit of the numbers up to n
        while n >= factor:
            # calculate the number of pairs of 0s and 1s for this bit
            pairs = (n + 1) // (factor * 2) * factor
    
            # calculate the number of leftover 1s for this bit
            ones = max(0, (n + 1) % (factor * 2) - factor)
    
            # add the count for this bit to the total count
            count += pairs + ones
    
            # update the factor to the next bit
            factor *= 2
    
        # return the count
        return count
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        ob=Solution()
        print(ob.countSetBits(int(input())))
# } Driver Code Ends