#User function Template for python3

class Solution:
    
    #Function to merge the arrays.
    def merge(self,arr1,arr2,n,m):
        #code here
        arr1_itr=n-1
        arr2_itr=0
        while arr1_itr>=0 and arr2_itr<m:
            if arr2[arr2_itr]<arr1[arr1_itr]:
                arr2[arr2_itr],arr1[arr1_itr]=arr1[arr1_itr],arr2[arr2_itr]
                arr1_itr-=1
                arr2_itr+=1
            else:
                break
        arr1.sort()
        arr2.sort()
    



#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n,m = map(int, input().strip().split())
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        ob=Solution()
        ob.merge(arr1, arr2, n, m)
        print(*arr1,end=" ")
        print(*arr2)
# } Driver Code Ends