class Solution:
	def overlappedInterval(self, Intervals):
	    Intervals.sort()
		ans=[Intervals[0]]
		for x,y in Intervals[1:]:
		    if x<=ans[-1][1]:
		        ans[-1][1]=max(y,ans[-1][1])
		    else:
		        ans.append([x,y])
	    return ans
		


#{ 
 # Driver Code Starts
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
    	n = int(input())
    	a = list(map(int, input().strip().split()))
    	Intervals = []
    	j = 0
    	for i in range(n):
    		x = a[j]
    		j += 1
    		y = a[j]
    		j += 1
    		Intervals.append([x,y])
    	obj = Solution()
    	ans = obj.overlappedInterval(Intervals)
    	for i in ans:
    		for j in i:
    			print(j, end = " ")
    	print()
# } Driver Code Ends