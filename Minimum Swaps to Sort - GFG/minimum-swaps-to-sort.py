

class Solution:
    
    #Function to find the minimum number of swaps required to sort the array.
	def minSwaps(self, nums):
		list1=[[v,i] for i,v in enumerate(nums)]
		list1.sort()
		i,count=0,0
		while i<len(nums):
		    j=list1[i][1]
		    if i==j:
		        i+=1
		        continue
		    list1[i],list1[j]=list1[j],list1[i]
	        count+=1
		return count


#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		obj = Solution()
		ans = obj.minSwaps(nums)
		print(ans)

# } Driver Code Ends