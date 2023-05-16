#User function Template for python3

class Solution:
    def romanToDecimal(self, s): 
        dic={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        number=0
        for i in range(len(s)-1):
            if dic[s[i]]<dic[s[i+1]]:
                number-=dic[s[i]]
            else:
                number+=dic[s[i]]
        return number+dic[s[-1]]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        ob = Solution()
        S = input()
        print(ob.romanToDecimal(S))
# } Driver Code Ends