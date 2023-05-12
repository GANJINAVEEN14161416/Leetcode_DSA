#User function Template for python3

class Solution:
    def sortBySetBitCount(self, arr, n):
        dic={}
        for i in range(n):
            dic[i] = bin(arr[i]).count("1")
        list1=sorted(dic.items(),key=lambda x:x[1],reverse=True)
        total=[]
        for i,v in list1:
            total.append(arr[i])
        arr[::]=total[::]
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