#User function Template for python3

class Solution:
    def removeConsecutiveCharacter(self, S):
        # code here
        word=""
        for i in range(len(S)-1):
            if S[i]==S[(i+1)]:
                continue
            else:
                word+=S[i]
        return word+s[-1]
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        s = input()
        ob = Solution()
        print(ob.removeConsecutiveCharacter(s))

# } Driver Code Ends