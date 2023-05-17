#{ 
 # Driver Code Starts

# } Driver Code Ends


def reverse(s):
    stack=[]
    for i in range(len(s)-1,-1,-1):
        stack.append(s[i])
    return "".join(stack)
        
    
    
    
    
    
    #Add code here

#{ 
 # Driver Code Starts.
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        str1=input()
        print(reverse(str1))
# } Driver Code Ends