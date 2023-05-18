#User function Template for python3

class Solution:
    def help_classmate(self, arr, n):
        list1=[-1]*n
        stack=[]
        for i in range(n):
            while stack and arr[i]<arr[stack[-1]]:
                index=stack.pop()
                list1[index]=arr[i]
            stack.append(i)
        return list1


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