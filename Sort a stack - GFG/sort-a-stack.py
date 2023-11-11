class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    def Sorted(self, s):
        # Code here
        def sort1(s):
            if len(s)==0:
                return 
            num=s.pop()
            sort1(s)
            merge(num)
        def merge(num):
            if not s or num>=s[-1]:
                s.append(num)
                return 
            temp=s.pop()
            merge(num)
            s.append(temp)
        return sort1(s)
    # def sorted(self, s):
    #     def merge(s):
    #         if len(s)==0:
    #             return 
    #         num=s.pop()
    #         merge(s)
    #         mergesort(s,num)
    #     def mergesort(s,num):
    #         if not s or num>=s[-1]:
    #             s.append(num)
    #             return 
    #         temp=s.pop()
    #         mergesort(s,num)
    #         s.append(temp)
    #     return merge(s)
                


        
            



#{ 
 # Driver Code Starts

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.Sorted(arr)
        for e in range(len(arr)):
            print(arr.pop(), end=" ")
        print()


# } Driver Code Ends