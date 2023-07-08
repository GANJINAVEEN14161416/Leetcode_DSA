
class Solution:
	def sortedArrayToBST(self, nums):
	    ans=[]
	    def BST(start,last,nums):
	        if start>last:
	            return
	        mid=(start+last)//2
	        ans.append(nums[mid])
	        BST(start,mid-1,nums)
	        BST(mid+1,last,nums)
	    BST(0,len(nums)-1,nums)
	    return ans


#{ 
 # Driver Code Starts

T=int(input())
for i in range(T):
	n = int(input())
	nums = list(map(int, input().split()))
	obj = Solution()
	ans = obj.sortedArrayToBST(nums)
	for _ in ans:
		print(_, end = " ")
	print()

# } Driver Code Ends