#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        dic={0:-1}
        prefix=0
        ans=0
        for i in range(n):
            prefix+=arr[i]
            if prefix in dic:
                ans=max(ans,i-dic[prefix])
            else:
                dic[prefix]=i
        return ans
        
        


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends