#User function Template for python3

class Solution:
    def segregateElements(self, arr, n):
        list1=[]
        for i in arr:
            if i>0:
                list1.append(i)
        for i in arr:
            if i<0:
                list1.append(i)
        arr[::]=list1[::]


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob=Solution()
        ob.segregateElements(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends