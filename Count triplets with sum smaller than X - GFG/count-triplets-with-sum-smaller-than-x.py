class Solution:
    def countTriplets(self, arr, n, sumo):
        arr.sort()
        count=0
        for i in range(n-2):
            left=i+1
            right=n-1
            while left<right:
                num=arr[i]+arr[left]+arr[right]
                if num<sumo:
                    count+=right-left # here is the 
                    left+=1
                else:
                    right-=1
        return count
                    
                


#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    t=int(input())
    for _ in range(0,t):
        l=list(map(int,input().split()))
        n=l[0]
        k=l[1]
        a=list(map(int,input().split()))
        ob = Solution()
        ans=ob.countTriplets(a,n,k)
        print(ans)
# } Driver Code Ends