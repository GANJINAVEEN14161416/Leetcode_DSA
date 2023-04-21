#User function Template for python3

def reverseWord(s):
    #your code here
    # if len(s)==0:
    #     return
    # else:
    #     return reverseWord(s[])+s
    m=""
    for i in s:
        m=i+m
    return m


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