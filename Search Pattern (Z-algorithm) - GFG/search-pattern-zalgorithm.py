#User function Template for python3

class Solution:
    def search(self, patt, s):
        # code here
        m,n=len(patt),len(s)
        list1=[]
        for i in range(n-m+1):
            if s[i:i+m]==patt:
                list1.append(i+1) 
        return list1 if list1 else [-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        if len(ans)==0:
            print("-1", end = " ")
        else:
            for value in ans:
                print(value,end = ' ')
        print()
# } Driver Code Ends