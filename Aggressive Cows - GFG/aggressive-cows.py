#User function Template for python3

class Solution:
    def solve(self,n,k,stalls):
        left,right=1,max(stalls)
        ans=0
        stalls.sort()
        def possible(mid):
            cows=1
            last=stalls[0]
            for i in stalls[1:]:
                if i-last>=mid:
                    cows+=1
                    last=i
            return cows>=k
        while left<=right:
            mid=(left+right)//2
            if possible(mid):
                ans=max(mid,ans)
                left=mid+1
            else:
                right=mid-1
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n, k = list(map(int, input().split()))
        stalls = list(map(int, input().split()))
        ob = Solution()
        res = ob.solve(n, k, stalls)
        print(res)

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends