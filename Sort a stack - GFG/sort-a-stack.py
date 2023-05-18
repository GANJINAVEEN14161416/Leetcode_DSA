class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    def sorted(self, s):
        if len(s)==0:
            return
        else:
            num=s.pop()
            self.sorted(s)
            self.sorted_num(s,num)
    def sorted_num(self,s,num):
        if len(s)==0 or num>=s[-1]:
            s.append(num)
            return 
        temp=s.pop()
        self.sorted_num(s,num)
        s.append(temp)



#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.sorted(arr)
        for e in range(len(arr)):
            print(arr.pop(), end=" ")
        print()


# } Driver Code Ends