#User function Template for python3

# arr[] : int input array of integers
# k : the quadruple sum required
class Solution:
    def fourSum(self, arr, k):
        list1=set()
        arr.sort()
        for i in range(n-3):
            for j in range(i+1,n-2):
                left=j+1
                right=n-1
                while left<right:
                    quad=arr[i]+arr[j]+arr[left]+arr[right]
                    if quad==k:
                        list1.add((arr[i],arr[j],arr[left],arr[right]))
                        left+=1
                    elif quad>k:
                    else:
                        left+=1
        return sorted(list(list1))
#User function Template for python3

# arr[] : int input array of integers
# k : the quadruple sum required
# class Solution:
#     def fourSum(self, arr, k):
#         if len(arr) < 4:
#             return -1
            
#         arr.sort()
#         check = set()
        
#         for i in range(0, n-3):
#             for j in range(i+1, n-2):
#                 left = j+1
#                 right = n-1
#                 while left < right:
#                     ssum = arr[i] + arr[j] + arr[left] + arr[right]
#                     if ssum > k:
#                         right -= 1
#                     elif ssum == k:
#                         temp = (arr[i], arr[j], arr[left], arr[right])
#                         check.add(temp)
#                         left += 1
#                     else:
#                         left += 1
                        
#         return sorted(list(check))
            
            
                            


#{ 
 # Driver Code Starts
#Initial Template for Python 3


#Main
if __name__=='__main__':
    t = int(input())
    while t:
        t-=1
        n, k=map(int,input().split())
        # print(n, k)
        a=list(map(int,input().strip().split()))[:n]
        # print(a)
        ob=Solution()
        ans=ob.fourSum(a, k)
        # print(ans)
        for v in ans:
            for u in v:
                print(u, end=" ")
            print("$", end="")
        if(len(ans)==0):
            print(-1, end="")
        print()
        
        

# } Driver Code Ends