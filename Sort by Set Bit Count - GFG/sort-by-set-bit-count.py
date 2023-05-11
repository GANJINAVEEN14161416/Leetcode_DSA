#User function Template for python3

class Solution:

    def sortBySetBitCount(self, a, n):
        ones = {}

        for i in range(n):
            ones[i]=bin(a[i]).count("1")
        ones = sorted(ones.items(),key = lambda item:item[1],reverse = True)
        list1=[]
        for i,v in ones:
            list1.append(a[i])
        a[::]=list1[::]
 

            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        ob.sortBySetBitCount(arr, n)
        print(*arr)

        T -= 1


if __name__ == "__main__":
    main()



# } Driver Code Ends