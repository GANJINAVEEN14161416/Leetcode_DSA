class Solution:
	def overlappedInterval(self, Intervals):
		Intervals.sort()
		list1=[Intervals[0]]
		for v1,v2 in Intervals[1:]:
		    if list1[-1][1]>=v1  :
		        list1[-1][1]=max(list1[-1][1],v2)
		    else:
		        list1.append([v1,v2])
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