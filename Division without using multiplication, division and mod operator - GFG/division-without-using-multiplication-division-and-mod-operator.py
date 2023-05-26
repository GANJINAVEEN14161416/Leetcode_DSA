#User function Template for python3

class Solution:
    def divide(self, a, b):
        sign=1
        if a<0 and b<0:
            sign=1
        elif a<0 or b<0:
            sign=-1
        a,b=abs(a),abs(b)
        result=0
        while (a-b)>=0:
            count=0
            while (a-(b<<1<<count))>=0:
                count+=1
            result+=1<<count
            a=a-(b<<count)
        return result*sign

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        inp = list(map(int,input().split())) 
        
        a=inp[0]
        b=inp[1]
        
        ob=Solution()
        
        print(ob.divide(a,b))
        
# } Driver Code Ends