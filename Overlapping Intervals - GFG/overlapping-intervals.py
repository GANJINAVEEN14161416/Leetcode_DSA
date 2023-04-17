class Solution:
	def overlappedInterval(self, Intervals):
	    Intervals.sort(key=lambda x:x[0])
		list1=[Intervals[0]]
		for i,j in Intervals[1:]:
		    if list1[-1][1]>=i:
		        list1[-1][1]=max(list1[-1][1],j)
		    else:
		        list1.append([i,j])
		return list1
		          
		           

		    


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