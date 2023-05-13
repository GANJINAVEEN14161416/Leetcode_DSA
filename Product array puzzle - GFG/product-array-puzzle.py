#User function Template for python3
class Solution:
    def productExceptSelf(self, nums, n):
        list1=[]
        if nums.count(0)>1:
            return [0]*n
        elif nums.count(0)==1:
            index=nums.index(0)
            nums.remove(0)
            product=1
            for i in nums:
                product*=i
            for i in range(n):
                if i==index:
                    list1.append(product)
                else:
                    list1.append(0)
            return list1
        else:
            product=1
            for i in nums:
                product*=i
            for i in range(n):
                list1.append(product//nums[i])
            return list1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())

    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]

        ans=Solution().productExceptSelf(arr,n)
        print(*ans)
# } Driver Code Ends