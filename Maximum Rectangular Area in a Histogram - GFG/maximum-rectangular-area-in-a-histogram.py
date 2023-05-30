#User function Template for python3


class Solution:
    
    #Function to find largest rectangular area possible in a given histogram.
    def getMaxArea(self,histogram):
        stack,maxarea=[],0
        for i,h in enumerate(histogram):
            start=i
            while stack and h<stack[-1][1]:
                index,hi=stack.pop()
                start=index
                maxarea=max(maxarea,(i-index)*hi)
            stack.append([start,h])
        for i,h in stack:
            maxarea=max(maxarea,(len(histogram)-i)*h)
        return maxarea
                
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

# by Jinay Shah 

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.getMaxArea(a))
# } Driver Code Ends