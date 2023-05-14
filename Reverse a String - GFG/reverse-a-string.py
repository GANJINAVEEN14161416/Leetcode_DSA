#User function Template for python3

def reverseWord(s):
    def reverse(s):
        if len(s) == 1:
            return s[0]
        else:
           return reverse(s[1:])+s[0]
    output=reverse(s)
    return output
    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        s = input()
        print(reverseWord(s))
        t = t-1

# } Driver Code Ends