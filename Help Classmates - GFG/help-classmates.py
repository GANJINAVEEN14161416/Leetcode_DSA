#User function Template for python3

class Solution:
    def help_classmate(self, arr, n):
        # Your code goes here
        # Return the list
        ans=[-1]*n
        stack=[]
        for i in range(n):
            while stack and arr[i]<arr[stack[-1]]:
                index=stack.pop()
                ans[index]=arr[i]
            stack.append(i)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [ int(x) for x in input().split() ]
        obj = Solution()
        result = obj.help_classmate(arr,n)
        for i in result:
            print(i,end=' ')
        print()

# } Driver Code Ends