#User function Template for python3

def searchPattern(st, pat):
    n=len(pat)
    for i in range(len(st)):
        if st[i:i+n]==pat:
            return True
    return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t=int(input())
for i in range(t):
    st=input()
    pat=input()
    if (searchPattern(st, pat)):
        print("Present")
    else:
        print("Not present")
# } Driver Code Ends